def make_heuristic():
    heuristic = {}
    with open("Heuristica.txt", "r") as file:
        for line in file.readlines():
            line = line.replace("\n", "")
            line_splitted = line.split(";")
            heuristic[f"{line_splitted[0]}"] = {"weight": None}
            heuristic[f"{line_splitted[0]}"]["weight"] = int(line_splitted[1])
    return heuristic
       
def make_graph():
    with open("Grafo.txt", "r") as file:
        graph = []
        for line in file.readlines():
            line = line.replace("\n", "")
            node = {"city1": "", "city2": "", "weight": None}
            line_splitted = line.split(";")
            node["city1"] = line_splitted[0]
            node["city2"] = line_splitted[1]
            node["weight"] = int(line_splitted[2])
            graph.append(node)
    return graph

def find_smallest_value(input_list):
    return min(input_list, key=lambda x: list(x.values())[0]['weight'])

old = "Arad"
destiny = "Bucareste"
heuristic = make_heuristic()
graph = make_graph()

actual_name = "Arad"
actual = {actual_name: {"weight": heuristic[actual_name]["weight"], "number_path_walked": 0, "path_walked": f"{actual_name}"}}

# A parada é quando chegar em Bucareste e o peso é o menor dos abertos
end = False
iteration = 1
node_opened = [{actual_name: {"weight": heuristic[actual_name]["weight"], "number_path_walked": 0}}]
print(f"#################  ITERAÇÃO 0  #################")
print(f"\nNós abertos:\n")
print(f"{actual_name} ({node_opened[0][actual_name]['weight']})")
print(f"\nNó que vai ser aberto: A cidade {actual_name} cujo o peso é {node_opened[0][actual_name]['weight']}\n")

while not end:
    old = actual_name
    print(f"#################  ITERAÇÃO {iteration}  #################")
    for connection in graph:
        if connection["city1"] == actual_name:
            node_opened.append({connection["city2"]: {"weight": heuristic[connection["city2"]]["weight"] + connection["weight"] + actual[actual_name]["number_path_walked"], "number_path_walked": actual[actual_name]["number_path_walked"] + connection["weight"], "path_walked": actual[actual_name]["path_walked"] + f" -> {connection['city2']}" }})
        if connection["city2"] == actual_name:
            node_opened.append({connection["city1"]: {"weight": heuristic[connection["city1"]]["weight"] + connection["weight"] + actual[actual_name]["number_path_walked"], "number_path_walked": actual[actual_name]["number_path_walked"] + connection["weight"], "path_walked": actual[actual_name]["path_walked"] + f" -> {connection['city1']}"}})
    # Remove o nó que foi aberto
    node_opened = [mapa for mapa in node_opened if actual_name not in mapa]
    print(f"\nNós abertos:\n")
    for node in node_opened:
        print(f"{list(node.keys())[0]} ({node[list(node.keys())[0]]['weight']})", end=" | ")
    print()
    actual = find_smallest_value(node_opened)
    actual_name = list(actual.keys())[0]
    if actual_name == "Bucareste":
        end = True
        break
    weight = actual[actual_name]["weight"]
    print(f"\nNó que vai ser aberto: A cidade {actual_name} cujo o peso é {weight}\n")
    for connection in graph:
        if (connection["city1"] == old or connection["city2"] == old) and (connection["city1"] == actual or connection["city2"] == actual):
            path_walked = path_walked + connection["weight"]
    iteration = iteration + 1
    

weight = actual[actual_name]["weight"]
print("\n\n--------------------------------------------------------------------\n")
print(f"O melhor custo é {weight}\n")
print("O melhor caminho é:")
print(actual[actual_name]["path_walked"])
print("\n\n--------------------------------------------------------------------\n")