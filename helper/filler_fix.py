
import json


def main():
    data = json.load(open('data.json'))

    mixed_canon = "46-47, 61, 68-69, 101, 354, 421, 489, 520, 574, 625, 628, 633, 653, 657, 679, 690, 731, 738, 751, 777-778, 789, 803, 807, 878-879, 881-885, 887-890, 924, 988-989, 991".replace(
        ' ', '')

    filler = "54-60, 98-99, 102, 131-143, 196-206, 220-226, 279-283, 291-292, 303, 317-319, 326-336, 382-384, 406-407, 426-429, 457-458, 492, 542, 575-578, 590, 626-627, 747-750, 780-782, 895-896, 907".replace(
        ' ', '')

    anime_canon = "50-51, 93, 213-216, 418-420, 453-456, 497-499, 506, 737, 775".replace(
        ' ', '')

    for i in range(len(data)):
        data[i]['mixed'] = False
        data[i]['filler'] = False
        data[i]['anime_canon'] = False

    for mixed_canon_range in mixed_canon.split(','):
        if '-' in mixed_canon_range:
            start, end = mixed_canon_range.split('-')
            for i in range(int(start), int(end) + 1):
                data[i - 1]['mixed'] = True
        else:
            data[int(mixed_canon_range) - 1]['mixed'] = True

    for filler_range in filler.split(','):
        if '-' in filler_range:
            start, end = filler_range.split('-')
            for i in range(int(start), int(end) + 1):
                data[i - 1]['filler'] = True
        else:
            data[int(filler_range) - 1]['filler'] = True

    for anime_canon_range in anime_canon.split(','):
        if '-' in anime_canon_range:
            start, end = anime_canon_range.split('-')
            for i in range(int(start), int(end) + 1):
                data[i - 1]['anime_canon'] = True
        else:
            data[int(anime_canon_range) - 1]['anime_canon'] = True

    json.dump(data, open('data_filler_fixed.json', 'w'), indent=4)


if __name__ == "__main__":
    main()
