import glob
import os
splits = ["negative", "positive"]
for _split in splits:
    all_paths = glob.glob(os.path.join(_split, "*.ann"))
    for path in all_paths:
        flag = False
        with open(path, "r", encoding='utf-8') as f_in:
            buf = f_in.readlines()
            for i in range(len(buf)):
                line = buf[i]
                if line[0] == "R":
                    if "\t" not in line:
                        flag = True
                        arr = line.split(" ")
                        assert len(arr) == 4
                        new_line = "{}\t{} {} {}".format(arr[0], arr[1], arr[2], arr[3])
                        buf[i] = new_line
                        assert "\n" in new_line
                        print(line, path)
        if flag:
            with open(path, "w", encoding='utf-8') as f_out:
                for line in buf:
                    f_out.write(line)

