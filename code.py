hctg = []
nodes = []
id1 = []
id2 = []
cost = []
pc = []
OPEN = []
CLOSED = []
etc = []


def list_add(a, b, c):
    for i in range(len(b)):
        x = b[i] + c[i]
        a.append(x)
    return a


def list_maker(a, b):
    lac = []
    for i in range(len(a)):
        l = []
        l.append(a[i])
        l.append((b[i]))
        lac.append(l)
    return lac


def dict_maker(a, b):
    c = {}
    for i in range(len(a)):
        c[str(a[i])] = str(b[i])
    return c


def rev(l):
    l.reverse()
    return l


node = open("nodes.csv", "r")
for x in node:
    x = str(x)
    if x[0] is not "#":
        ln = x.split(",")
        hctg.append(float(ln[3]))
        nodes.append(int(ln[0]))
node.close()
edge = open("edges.csv", "r")
for x in edge:
    x = str(x)
    if x[0] is not "#":
        le = x.split(",")
        id1.append(int(le[1]))
        id2.append(int(le[0]))
        cost.append(float(le[2]))
# initialization
for i in range(1, len(nodes) + 1):
    if i == 1:
        pc.append(0)
    else:
        pc.append(float("inf"))
HCTG = dict_maker(nodes, hctg)
PC = dict_maker(nodes, pc)
list_add(etc, pc, hctg)
par = [None for i in range(len(nodes))]
PAR = dict_maker(nodes, par)
node_rel = list_maker(id1, id2)
EDGES = dict_maker(node_rel, cost)
TC = dict_maker(nodes, etc)
ETC = list_maker(nodes, etc)
OPEN.append(min(ETC, key=lambda ETC: ETC[1]))
goal_node = nodes[len(nodes) - 1]
# exploration node wise
while len(OPEN) is not 0:
    OPEN = sorted(OPEN, key=lambda OPEN: OPEN[1])
    current = OPEN[0][0]
    CLOSED.append(OPEN[0][0])
    OPEN.remove(OPEN[0])
    nbr = []
    for i in range(len(node_rel)):
        if node_rel[i][0] == current:
            nbr.append(node_rel[i][1])
    for i in nbr:
        if i not in CLOSED:
            a = "[" + str(current) + "," + " " + str(i) + "]"
            new_pc = float(EDGES.get(a))
            new_etc = new_pc + float(HCTG[str(i)])
            if float(TC[str(i)]) > new_etc:
                TC[str(i)] = str(new_etc)
                ETC[i - 1][1] = new_etc
                PAR[str(i)] = str(current)
                OPEN.append(ETC[i - 1])
path = []
path.append(goal_node)
par = PAR[str(goal_node)]
path.append(par)
while par is not None:
    par = PAR[par]
    if par == str(None):
        break
    else:
        path.append(par)
path = [int(i) for i in path]
path = rev(path)
path_file = open("Path_project.csv", "w")
path_file.write(str(path)[1 : len(str(path)) - 1])
