""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
def get_path(filename):
    """
    :param filename: имя файла, который надо найти в директориях ниже
    :return: возвращает полный путь до файла
    """
    import os
    for (dirname, sub, file) in os.walk(os.getcwd()):
        if 'dna.fasta' in file:
            return os.path.join(dirname, filename)

dna = get_path('dna.fasta')
rna_codon = get_path('rna_codon_table.txt')


def translate_from_dna_to_rna(dna):
    """your code here"""
    # open file, start reading and replacing
    with open(dna, 'r') as f:
        # next(f)     # skip first line
        rna = ''
        for line in f:
            if line.strip().startswith('>'):
                rna += f"{line.strip()}\n"
                continue
            rna += line.strip().replace('T', 'U')+'\n'

    # write result to file
    with open('dna_to_rna.txt', 'w') as out:
        out.write(rna)
    return rna


def count_nucleotides(dna):

    """your code here"""
    nucls = ['A', 'C', 'G', 'T']
    HSBGPG = {i: 0 for i in nucls}
    HSGLTH1 = {i: 0 for i in nucls}
    switcher = 0

    with open(dna, 'r') as f:
        next(f)     # skip first line
        for line in f:
            if line.startswith('>HSGLTH1'):
                switcher = 1
                continue

            if switcher == 0:
                for nucl in nucls:
                    HSBGPG[nucl] += line.strip().count(nucl)

            if switcher == 1:
                for nucl in nucls:
                    HSGLTH1[nucl] += line.strip().count(nucl)

        print(
            'HSBGPG: ',
            'A --', HSBGPG['A'],
            'C --', HSBGPG['C'],
            'G --', HSBGPG['G'],
            'T --', HSBGPG['T'],
            'HSGLTH1: ',
            'A --', HSGLTH1['A'],
            'C --', HSGLTH1['C'],
            'G --', HSGLTH1['G'],
            'T --', HSGLTH1['T'], '\n'
              )
    with open('statistic_of_nucleotides_in_DNA.txt', 'w') as out:
        out.write(
f"""
    HSBGPG:
        A -- {HSBGPG['A']},
        C -- {HSBGPG['C']},
        G -- {HSBGPG['G']},
        T -- {HSBGPG['T']},

    HSGLTH1:
        A -- {HSGLTH1['A']},
        C -- {HSGLTH1['C']},
        G -- {HSGLTH1['G']},
        T -- {HSGLTH1['T']}"""
        )
    return HSBGPG, HSGLTH1


def translate_rna_to_protein(rna, rna_codon):

    """your code here"""
    rna_codon_dict = {}     # dict with codes
    with open(rna_codon) as f:
        # lets convert lines to dict
        for line in f:
            data = line.split()
            values = [data[x] for x in range(1, len(data), 2)]
            keys = [data[x] for x in range(0, len(data), 2)]
            temp_dict = dict(zip(keys, values))
            rna_codon_dict.update(temp_dict)


    protein = ""
    # now check each line by cutting for 3 letters
    # with step 3 and use as key for dict rna_codon_dict
    for line in rna:
        if line.strip().startswith('>'):
            protein += f"\n{line.strip()}\n"
            continue
        if len(line) % 3 == 0:
            for i in range(0, len(line), 3):
                codon = line[i:i + 3]
                protein += rna_codon_dict[codon]

    # print(rna_codon_dict)
    print(protein)
    with open('rna_to_protein.txt', 'w') as out:
        out.write(protein)

    return protein


count_nucleotides(dna)
rna = str(translate_from_dna_to_rna(dna)).split('\n')
translate_rna_to_protein(rna, rna_codon)
