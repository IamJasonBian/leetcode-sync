class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        cities_with_outgoing_paths = set()

        # array paths
        # paths[i] = [cityA_i, cityB_i]
        # destination city (city without any path outgoing to another city)

        '''
        All possible trips are: 
        "D" -> "B" -> "C" -> "A". 
        "B" -> "C" -> "A". 
        "C" -> "A". 
        "A". 
        '''

        for path in paths:
            # If we add everything in the origin city, then outgoing cities would not have to exist
            cities_with_outgoing_paths.add(path[0])
        
        # One more pass to find the destination city
        for path in paths:

            if path[1] not in cities_with_outgoing_paths:
                return path[1]
        
        return ""

