import pyperclip

def comma_delim_repeat(t: str, count: int) -> str:
    output = list(map(lambda l : t if l == count-1 else f"{t}, ", [i for i in range(count)]))
    return "".join(output)

def main() -> None:
    print("Hello, world")
    raw_text = pyperclip.paste()
    print(raw_text)

    num_cols = len(raw_text.split("\n")[0].split("\t"))

    result = f'''#figure(caption: "CAPTION HERE", table(
  columns: ({comma_delim_repeat('auto', num_cols)}),
  align: horizon,
        {''.join(['[], ' for _ in range(num_cols)])}
        '''

    for line_num, line in enumerate(line_list:=raw_text.split("\n")):
        for c in filter(lambda s : not s.strip() == "",line.split("\t")):
            result += f"[{c}], "
        result+="\n" if not line_num == len(line_list)-1 else ""

    result += '''))'''

    print(result)

if __name__ == "__main__":
    main()
