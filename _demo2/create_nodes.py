import random
import sys

idx = 0

for i in range(int(sys.argv[1])):    
    print "<li rel='drive' id='node_" + str(idx) + "'><ins class='jstree-icon'>&#160;</ins><a href=''><ins class='jstree-icon'>&#160;</ins>Node title</a>",
    idx += 1
    print "<ul>",
    for j in range(random.randint(1, 10)):
        print "<li rel='folder' id='node_" + str(idx) + "'><ins class='jstree-icon'>&#160;</ins><a href=''><ins class='jstree-icon'>&#160;</ins>Node title</a>",
        idx += 1
        print "<ul>",

        for k in range(random.randint(1, 10)):
            print "<li rel='default' id='node_" + str(idx) + "'><ins class='jstree-icon'>&#160;</ins><a href=''><ins class='jstree-icon'>&#160;</ins>Node title</a></li>",
            idx += 1

        print "</ul></li>",
    print "</ul></li>"
