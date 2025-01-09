
from Terrain import Terrain, Case

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []

class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # Trouver l'entrée
        entree = t.get_entree()
        if entree == (-1, -1):  # Si aucune entrée n'est trouvée
            print("Aucune entrée trouvée.")
            return -1, {}, []

        # Trouver les clients
        clients = t.get_clients()
        if not clients:  # Si aucun client n'est trouvé
            print("Aucun client trouvé.")
            return -1, {}, []

        # Configurer les nœuds
        noeuds = {0: entree}  # Nœud 0 pour l'entrée
        for i, client in enumerate(clients):
            noeuds[i + 1] = client  # Associer chaque client à un identifiant unique

        # Configurer les arcs : connecter chaque client à l'entrée
        arcs = [(0, i + 1) for i in range(len(clients))]

        # Ordre de distribution : entrée suivie des clients
        distribution = list(noeuds.keys())

        return 0, noeuds, arcs


