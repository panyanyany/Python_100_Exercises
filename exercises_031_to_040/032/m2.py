def ticktock():
    if not hasattr(ticktock, 'counter'):
        ticktock.counter = 0
    print(f'欢迎光临，这是你第 {ticktock.counter} 次来了!')
    ticktock.counter += 1


ticktock()
ticktock()
ticktock()
