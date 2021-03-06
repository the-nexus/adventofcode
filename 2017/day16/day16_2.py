filename = "./day16/day16_input.txt"
input_file = open(filename)
lines = input_file.readline().split(",")

n_dances = 1000000000
dance_idx = 0
n_programs = 16
programs = [chr(idx + 97) for idx in range(n_programs)]
first_programs_str = "".join(programs)

while dance_idx < n_dances:
    for line in lines:
        instruction = line[0]
        str_args = line[1:].split("/")
        if instruction == "s":
            spin = int(str_args[0]) % n_programs
            programs = [programs[(idx - spin) % n_programs] for idx in range(n_programs)]
        elif instruction == "x":
            idx_a = int(str_args[0])
            idx_b = int(str_args[1])
            temp_val = programs[idx_a]
            programs[idx_a] = programs[idx_b]
            programs[idx_b] = temp_val
        elif instruction == "p":
            idx_a = programs.index(str_args[0])
            idx_b = programs.index(str_args[1])
            temp_val = programs[idx_a]
            programs[idx_a] = programs[idx_b]
            programs[idx_b] = temp_val
    dance_idx = dance_idx + 1

    programs_str = "".join(programs)

    if programs_str == first_programs_str:
        n_dances = (n_dances % dance_idx) + dance_idx
         
    

print("The order of the programs is:", "".join(programs))
