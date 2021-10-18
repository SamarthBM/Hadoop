import subprocess

def run_cmd(args_list):
    """
    Description:
        this function execute CLI commands
    """
    print('Running systrm command: {0}'.format(' '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err


version= run_cmd(['hadoop', 'version'])
print(version)

new_directory= run_cmd(['hadoop', 'fs', '-mkdir', '/HadoopSample1'])
print(new_directory)

list_all_directory= run_cmd(['hadoop', 'fs', '-ls', '/'])
print(list_all_directory)

put_command= run_cmd(['hadoop', 'fs', '-put', '/home/samarth/Data-Engg/Hadoop/WordCountProgram/input.txt', '/HadoopSample1'])
print(put_command)

copy_from_local= run_cmd(['hadoop', 'fs', '-copyFromLocal', '/home/samarth/Data-Engg/Hadoop/WordCountProgram/input1.txt', '/HadoopSample1'])
print(copy_from_local)

cat= run_cmd(['hadoop', 'fs', '-cat', '/HadoopSample1/input.txt'])
print(cat)

get= run_cmd(['hadoop', 'fs', '-get', '/HadoopSample1/input.txt', '/home/samarth/Data-Engg/Hadoop/CopyFromHadoop'])
print(get)

copy_to_local= run_cmd(['hadoop', 'fs', '-copyToLocal', '/HadoopSample1/input1.txt', '/home/samarth/Data-Engg/Hadoop/CopyFromHadoop'])
print(copy_to_local)

copy= run_cmd(['hadoop', 'fs', '-cp', '/HadoopSample1/input1.txt', '/sample'])
print(copy)

# remove_directory= run_cmd(['hadoop', 'fs', '-rm', '-R', '/HadoopSample1'])
# print(remove_directory)