rotation = "clock"
n_str = 3
a = "This Is A Test String"
if rotation == "anti":
    a = a[len(a)-n_str::] + a[:len(a)-n_str:]
elif rotation == "clock":
    a = a[n_str::] + a[:n_str:]
print(a)
