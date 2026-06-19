titles = ["R45: შესავალი React-სა და Next-ში","R46: JSX და Prop", "R47: Next.js-ის სტრუქტურა Part 1", "R48: პირველი Jira-ს ტასკი, component render patterns",
"R49: State, User input"," R55: ასინქრონული პროგრამირება, Promise", "R56: Component lifecycle, Effects", "R57: browser-ის ინფორმაციული საცავები", "R58: Recoil ანუ კომპონენტშორისი state-ი",
"R61: React-ის სხვა hook-ები", "R63: Promise Part 2, async await"]

contents = [
"""
პრეზენტაცია: https://miro.com/app/board/uXjVMGtN0rA=/?share_link_id=791706969694
ჩანაწერი: https://youtu.be/NFRJO3au6ns

შეხვედრის ჩანაწერი:
https://youtu.be/WGLMRNgj4ZI 
""",
"""პრეზენტაცია: https://miro.com/app/board/uXjVMGdRGsM=/?share_link_id=1210746149
ჩანაწერი: https://www.youtube.com/watch?v=XJshOU-GXtM""",
"ჩანაწერი: https://www.youtube.com/watch?v=W2ZATjq2XDU",
"""პრეზენტაცია: https://miro.com/app/board/uXjVMDv-aZE=/?share_link_id=57566335532
ჩანაწერი: https://youtu.be/xWKa4LFVt5Q
""",
"""პრეზენტაცია: https://miro.com/app/board/uXjVMCpHTqo=/?share_link_id=505227585457
ჩანაწერი: https://youtu.be/ilX4DgLccws""",
"""პრეზენტაცია: https://miro.com/app/board/uXjVM9amGhw=/?share_link_id=147538586381
ჩანაწერი: https://youtu.be/4t6XOuaDxJE"""
"""პრეზენტაცია: https://miro.com/app/board/uXjVM_2bm1g=/?share_link_id=854678760671
ჩანაწერი: https://youtu.be/qUjnVPltrk8""",
"""ჩანაწერი: https://miro.com/app/board/uXjVM7zQfdo=/?share_link_id=403822821462
პრეზენტაცია: https://www.youtube.com/watch?v=k3kP1JgnfS0""", 
"""პრეზენტაცია: https://miro.com/app/board/uXjVM62jKso=/?share_link_id=316311206424
ჩანაწერი: https://youtu.be/z_9oP_Xv9TY""", 
"""პრეზენტაცია: https://miro.com/app/board/uXjVM4KSZog=/
ჩანაწერი: https://youtu.be/nZ4EVRZns_Q

შეხვედრის ჩანაწერი:
https://youtu.be/ZqpjbG-bDXc """,
"""პრეზენტაცია: https://react.dev/reference/react
ჩანაწერი: https://youtu.be/yV6-UqCvUz0""",
"""პრეზენტაცია: https://miro.com/app/board/uXjVM4i-0KY=/?share_link_id=831590592123
ჩანაწერი: https://youtu.be/C9B86-qTusc"""
]

for i in range(len(titles)):
    filename = f"{titles[i]}.txt"

    with open(filename, "w") as f:
        f.write(contents[i])

    print(f"Saved {filename}")