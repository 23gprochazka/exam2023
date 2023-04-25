from function.data import n, min_score, scores # imports all demo data



def sort_data(data): # sorts given data by value
    sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True) # sorts given data by their value from higher to lower
    return(sorted_scores)



def limit_data(data, limit, minimum): # sorts and limits given data by limit
    n_scores = []
    
    if len(data) < n: #  if n is greater than number of given data
        print("Stanovený počet nejlepších studentů je větší, než množství studentů!") # prints notification
        limit = len(data) # sets limit to all data
    
    for score in range(limit):
        if int(sort_data(data)[score][1]) >= minimum: # adds only data with value grater than minimum
            n_scores.append(sort_data(data)[score]) # leaves just x highest data in sorted data by given limit
        
    n_scores = dict(n_scores) # converts to dictionary
    
    if len(n_scores) != limit: # adds notification when there are not enough data
        print("Neexistuje tolik studentů s požadovaným minimálním skóre! Zobrazeni jsou ti, kteří tohoto skóre dosáhli.")
    
    return(n_scores)




def nice_print(data): # prints given data in better formating
    for key, value in data.items():
        print(f"{key} ({value})") # print using f-print
    
nice_print(limit_data(scores, n, min_score)) # limit (and sort) scores by n and print it nicely
