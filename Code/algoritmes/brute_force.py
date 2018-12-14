class Brute_force(object):

    def bfs(self, materix, start, visited=[]):
        ''' Run Brute Force switch '''
        visited = visited+[start]
        paths = []
        list = materix.get(start.id)

        if len(visited) == 5:
            return[visited]
        else:
          for house in list:
              if house not in visited:
                  newpaths = self.bfs(Brute_force, materix, house, visited)
                  for newpath in newpaths:
                      paths.append(newpath)
        return paths
