import urllib2

data = urllib2.urlopen('https://projecteuler.net/project/resources/p081_matrix.txt').read()
data = data.split('\n')
matrix = [map(int, line.split(',')) for line in data[:-1]]

# dynamic programming

path_sum = [0 for i in xrange(len(matrix[0]))]

prev_line = [0 for i in xrange(len(matrix[0]))]
prev_line[0] = matrix[0][0]
for j in xrange(1, len(matrix[0])):
    prev_line[j] = prev_line[j-1] + matrix[0][j]
    
for i in xrange(1, len(matrix)):
    path_sum[0] = prev_line[0] + matrix[i][0]
    for j in xrange(1, len(matrix[i])):
        path_sum[j] = min(prev_line[j], path_sum[j-1]) + matrix[i][j]
    prev_line = path_sum[:]

print path_sum[-1]
