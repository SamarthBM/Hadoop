1. Create a directory to save all the files related to word length program.

	mkdir Matrix


2. Create a text file inside the created directory to store data in it.

	touch input.txt
	nano input.txt. To edit the txt file


3. Create a mapper.py file to write the map function code.

	nano mapper.py



4. Execute the mapper.py file

	cat input.txt| python3 mapper.py


5. Create a reducer.py file to write the reduce function code.

	nano reducer.py


6. Execute the mapper.py and reducer.py file

	cat input.txt| python3 mapper.py | sort |  python3 reducer.py 


7. Start all apache hadoop daemons

	start-all.sh


8. Create a directory in hadoop

	hadoop fs -mkdir /Matrix


9. Copy the data file from local system to hadoop system

	hadoop fs -put /home/samarth/Data-Engg/Hadoop/Map-Reduce-Programs/Matrix/input.txt /Matrix


10. Use the jar file, mapper and reducer file to execute the program

	hadoop jar /home/samarth/Data-Engg/Hadoop/jar-files/hadoop-streaming-3.3.1.jar \
	-file /home/samarth/Data-Engg/Hadoop/Map-Reduce-Programs/Matrix/mapper.py -mapper "python3 mapper.py" \
	-file /home/samarth/Data-Engg/Hadoop/Map-Reduce-Programs/Matrix/reducer.py -reducer "python3 reducer.py" \
	-input /Matrix/input.txt \
	-output /Matrix/Output


11. Use cat command to check the output file

    	hadoop fs -cat /Matrix/Output/part-00000

