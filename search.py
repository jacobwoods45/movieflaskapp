import csv


class MovieSearch:
        suggestionResults = {
            "DisneyPlus" : [],
            "Netflix": [],
            "Hulu": [],
            "Amazon": []
        }
        
        def prettifySuggestions(suggestions):
            if type(suggestions) == list:
                for service in suggestions:
                    print("Found an exact match: ")
                    print(service)
            else:
                for service in suggestions:
                    print(service)
                    for suggestion in suggestions[service]:
                        print("\t" + suggestion)

        def dynamicSearch(movie):
            services_with_exact_matches = MovieSearch.searchAllPlatforms(movie)
            if services_with_exact_matches:
                return services_with_exact_matches
            else:
                print("NO EXACT RESULTS FOUND, SUGGESTONS INCLUDE: ")
                return MovieSearch.searchAllPlatformsSuggestions(movie)
        def searchAllPlatformsSuggestions(movie):
            titles = ["DisneyPlus", "Netflix", "Amazon", "Hulu"]
            servicesFound=[] ##Array of all of the services where that title was found
            for title in titles:
                if MovieSearch.searchSuggestions(movie, title):
                    MovieSearch.suggestionResults[title] = MovieSearch.searchSuggestions(movie, title)
            return MovieSearch.suggestionResults
            
        def searchAllPlatforms(movie):
            titles = ["DisneyPlus", "Netflix", "Amazon", "Hulu"]
            servicesFound=[] ##Array of all of the services where that title was found
            for title in titles:
                if MovieSearch.searchExact(movie, title) == True :
                    servicesFound.append(title)
                elif MovieSearch.searchExact(movie.title(), title) == True:
                    servicesFound.append(title)
            return servicesFound

        def searchExact(movie, service):

            csvfile = ""
            exact_results = []  

            if service == "DisneyPlus" or service == "disneyplus" or service == "disney plus":
                csvfile = "disney_plus_titles.csv"
            elif service == "Netflix" or service == "netflix":
                csvfile = "netflix_titles.csv"
            elif service == "Amazon" or service == "amazon prime" or service == "amazon" or service == "Amazon Prime":
                csvfile = "amazon_prime_titles.csv"
            elif service == "Hulu" or service == "hulu":
                csvfile = "hulu_titles.csv"
            else:
                print("NOT VALID ARGUEMENT")

            with open(csvfile, encoding='utf-8') as f_obj:
                reader = csv.reader(f_obj, delimiter=',')
                for line in reader:
                    if movie == line[2]:
                        exact_results.append(line[2])
                if exact_results:
                    return True
                else:
                    return False

        def searchSuggestions(movie, service):
            csvfile = ""
            suggestions = []


            if service == "DisneyPlus" or service == "disneyplus" or service == "disney plus":
                csvfile = "disney_plus_titles.csv"
            elif service == "Netflix" or service == "netflix":
                csvfile = "netflix_titles.csv"
            elif service == "Amazon" or service == "amazon prime" or service == "amazon" or service == "Amazon Prime":
                csvfile = "amazon_prime_titles.csv"
            elif service == "Hulu" or service == "hulu":
                csvfile = "hulu_titles.csv"
            

            with open(csvfile, encoding='utf-8') as f_obj:
                reader = csv.reader(f_obj, delimiter=',')
                for line in reader:
                    if movie in (" " + line[2] + " ") :
                        suggestions.append(line[2])
                    if movie in (" " + line[2].capitalize() + " ") :
                        suggestions.append(line[2])
                if suggestions:
                    return suggestions
                else:
                    return False
        