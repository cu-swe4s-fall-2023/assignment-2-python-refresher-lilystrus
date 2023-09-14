def get_column(file_name, query_column, query_value, result_column):
    
    ResultList = []
    
    file = open(file_name,'r')
    for line in file:
        ListofLine = line.strip().split(',')
        if ListofLine[query_column-1] == query_value:
            ResultList.append(ListofLine[result_column-1])

    file.close()
   
    return ResultList
   
