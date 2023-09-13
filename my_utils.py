def get_column(file_name, query_column, query_value, result_column):
    
    ResultList = []
    
    file = open(file_name,'r')
    for line in file:
        ListofLine = line.strip().split(',')
        if ListofLine[query_column] == query_value:
            ResultList.append(ListofLine[result_column])

    file.close()
   
    return ResultList
   
