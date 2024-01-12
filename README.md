# PythonSketchbook

## Dictionary und For-Loop Erklärung

1. students = {"Fabian": None, "Sebastian": None, "Kevin": None, "Mohamad": None}: 
Diese Zeile erstellt ein Wörterbuch namens students. Das Wörterbuch hat vier Schlüssel 
("Fabian", "Sebastian", "Kevin", "Mohamad"), jeder mit einem Wert von None.

2. for student in students:: Diese Zeile startet eine for-Schleife. Die for-Schleife 
wird über jeden Schlüssel im students Wörterbuch iterieren. In jeder Iteration wird die 
Variable student auf einen der Schlüssel gesetzt.

3. students[student] = 1: Innerhalb der for-Schleife setzt diese Zeile den Wert des 
aktuellen Schlüssels (dargestellt durch student) auf 1. Dies wird für jeden Schlüssel 
im Wörterbuch durchgeführt, so dass nach dieser for-Schleife alle Werte im students Wörterbuch 1 sein werden.

4. for student in students:: Diese Zeile startet eine weitere for-Schleife, 
die wieder über jeden Schlüssel im students Wörterbuch iteriert.

5. print(f"{student} hat die Note {students[student]} "): Innerhalb der 
zweiten for-Schleife druckt diese Zeile eine Zeichenkette für jeden Schüler aus. 
Die Zeichenkette enthält den Namen des Schülers (den aktuellen Schlüssel, dargestellt durch student) 
und seine Note (den Wert, der mit dem aktuellen Schlüssel im students Wörterbuch verknüpft ist).

Die Gesamtwirkung dieses Codes besteht also darin, alle Schülernoten auf 1 zu 
setzen und dann den Namen und die Note jedes Schülers auszudrucken.