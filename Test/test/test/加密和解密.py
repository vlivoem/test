from tkinter import messagebox, simpledialog, Tk
import tkinter


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message


def get_task():
    task = simpledialog.askstring('任务', '你是否想要加密或解密信息?')
    return task


def get_message():
    message = simpledialog.askstring('信息', '输入相关信息: ')
    return message


root = Tk()
while True:
    task = get_task()
    if task == '加密':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('密电的密文为:', encrypted)

    elif task == '解密':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('密电的明文为:', decrypted)
    else:
        break
root.mainloop()

# def test():
#     # # 主窗口：
#     # window = tkinter.Tk()  # 创建窗口
#     # window.title("简易版小程序")  # 设置标题
#     # window.geometry("500x300")
#     #
#     # # 创建控件容器frameDemo1
#     # frameDemo1 = tkinter.Frame(window)
#     #
#     # # 向frameDemo1中加入组件
#     # label_1 = tkinter.Label(frameDemo1, text="标签1文本")
#     # label_2 = tkinter.Label(frameDemo1, text="标签2文本")
#     # label_1.pack()
#     # label_2.pack()
#     #
#     # # 将该控件容器加入到窗口中
#     # frameDemo1.pack()
#     #
#     # window.mainloop()  # 将窗口显示出来
#     root = Tk()
#     tl = tkinter.Toplevel()
#     # 为了区别root和tl，我们向tl中添加了一个Label
#     tkinter.Label(tl, text='hello label').pack()
#     root.mainloop()


if __name__ == "__main__":
    print()