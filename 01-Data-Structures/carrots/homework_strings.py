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




def translate_from_dna_to_rna(dna):
    
    """your code here"""
    
    return rna


def count_nucleotides(dna):
    
    """your code here"""

    with open(dna, 'r') as f:
        lines = f.readlines()[1::]

        nucleotides = ['A', 'C', 'G', 'T']
        HSBGPG = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        HSGLTH1 = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        switcher = 0

        for i in range(len(lines)):
            if '>' in lines[i].strip():
                switcher = 1

            if switcher == 0:
                for nucleotide in nucleotides:
                    if nucleotide == 'A':
                        HSBGPG[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'C':
                        HSBGPG[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'G':
                        HSBGPG[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'T':
                        HSBGPG[nucleotide] += lines[i].strip().count(nucleotide)
            else:
                for nucleotide in nucleotides:
                    if nucleotide == 'A':
                        HSGLTH1[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'C':
                        HSGLTH1[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'G':
                        HSGLTH1[nucleotide] += lines[i].strip().count(nucleotide)
                    if nucleotide == 'T':
                        HSGLTH1[nucleotide] += lines[i].strip().count(nucleotide)

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
            'T --', HSGLTH1['T']
              )

    return HSBGPG, HSGLTH1


def translate_rna_to_protein(rna):
    
    """your code here"""
    
    return protein

count_nucleotides(dna)