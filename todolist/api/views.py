import csv
import json

from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from task.models import File, Player

from .serializers import FileSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """Class ViewSet for players"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path=r'from_last_file'
    )
    def get_players(self, request):
        """Collects players for last file."""
        last_id = File.objects.latest('id').id
        players = Player.objects.filter(file=last_id)
        serializer = PlayerSerializer(players, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK)


def int_score(list_results=None):
    """Сalculates score for players in list
    using coefficients A, B, C from file constants.json."""
    f = open('api/constants.json')
    const = json.load(f)
    for result in list_results:
        score = 0
        for key, value in result.items():
            if const.get(key) is not None:
                A = const[key]['A']
                B = const[key]['B']
                C = const[key]['C']
                point = int(A * abs(B - value)**C)
                score += point
        result['score'] = score
    return list_results


def in_sec(min_sec):
    """Transforms value like xx.xx.xx in seconds."""
    list_sec = min_sec.split('.')
    return int(list_sec[0]) * 60 + int(list_sec[1]) + float(list_sec[1]) / 100


def sort_by_score(score_list=None):
    """Sorts list by field score."""
    sorted_list = sorted(
        score_list,
        key=lambda x: - x['score']
    )
    for i, x in enumerate(sorted_list):
        x['place'] = str(i + 1)
    return sorted_list


def edit_place(sort_list):
    """Edits places if players have same results."""
    i = 0
    while i < len(sort_list):
        double_list = [i]
        for j in range(i + 1, len(sort_list)):
            if sort_list[i]['score'] == sort_list[j]['score']:
                double_list.append(j)
        if len(double_list) > 1:
            for y in double_list:
                sort_list[y]['place'] = (
                    f'{double_list[0]+1}'
                    f'-{double_list[-1]+1}'
                )
        i = double_list[-1] + 1
    return sort_list


def del_old_files(new_file):
    """Removes past files from DataBase and folder media."""
    files = File.objects.all()
    for file in files:
        if file != new_file:
            file.delete()


def create_list_results(filename):
    """Creates list of players from initial csv file."""
    results = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            result = {
                'name': row[0],
                '100 metres': float(row[1]),
                'Long jump': int(float(row[2])*100),
                'Shot put': float(row[3]),
                'High jump': int(float(row[4])*100),
                '400 metres': float(row[5]),
                '110 metres hurdles': float(row[6]),
                'Discus throw': float(row[7]),
                'Pole vault': int(float(row[8])*100),
                'Javelin throw': float(row[9]),
                '1500 metres': in_sec(row[10]),
            }
            results.append(result)
    return results


def create_players(new_file):
    """Creates players in DataBase."""
    f = open('media/RESULT.json')
    players = json.load(f)
    for player in players:
        results = (
            f'{player["100 metres"]} - '
            f'{player["Long jump"]} - '
            f'{player["Shot put"]} - '
            f'{player["High jump"]} - '
            f'{player["400 metres"]} - '
            f'{player["110 metres hurdles"]} - '
            f'{player["Discus throw"]} - '
            f'{player["Pole vault"]} - '
            f'{player["Javelin throw"]} - '
            f'{player["1500 metres"]}'
        )
        Player.objects.create(
            file=new_file,
            name=player['name'],
            score=player['score'],
            position=player['place'],
            results=results,
        )


def input_initial_values(position_list, filename):
    """Changes values to initial if they were transformed"""
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            for player in position_list:
                if row[0] == player['name']:
                    player['Long jump'] = float(row[2])
                    player['High jump'] = float(row[4])
                    player['Pole vault'] = float(row[8])
                    player['1500 metres'] = row[10]
    return position_list


class FileViewSet(viewsets.ModelViewSet):
    """Class ViewSet for files."""
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path=r'download_json'
    )
    def load_json(self, request):
        """Loads json file with results"""
        new_file = File.objects.latest('id')
        del_old_files(new_file)
        results = create_list_results(f'media/{new_file.file}')
        score_list = int_score(results)
        sort_list = sort_by_score(score_list)
        position_list = edit_place(sort_list)
        final_list = input_initial_values(
            position_list,
            f'media/{new_file.file}'
        )
        filename = "media/RESULT.json"
        with open(filename, 'w') as json_file:
            json.dump(
                final_list,
                json_file,
                indent=4,
                separators=(',', ': '))
        create_players(new_file)
        res_file = open(filename, "r")
        return HttpResponse(res_file, content_type='text/plain')
