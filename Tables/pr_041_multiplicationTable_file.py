
for i in range(1,21):
        for j in range(1, 11):
            with open(f"Tables/Table of {i}.txt", 'a') as f:
                num = f"{i}X{j}={i*j}\n"
                f.write(num)
