import random
import time

def basketball_game():
    print("=========================================")
    print("🏀 歡迎來到《最後一擊：絕殺時刻》籃球挑戰賽 🏀")
    print("=========================================")
    print("比賽剩餘最後 30 秒，你落後對手 2 分！")
    print("你有 3 次進攻機會，請帶領球隊逆轉勝吧！\n")

    player_score = 80
    opponent_score = 82
    possessions = 3

    while possessions > 0:
        print(f"⏱️ 剩餘進攻次數: {possessions} 次")
        print(f"📊 目前比分 -> 你: {player_score} | 對手: {opponent_score}")
        print("-----------------------------------------")
        print("請選擇你的進攻戰術：")
        print("1. 🎯 中距離跳投（兩分球，成功率 55%）")
        print("2. 🔥 外線三分彈（三分球，成功率 35%）")
        print("3. ⚡ 強入禁區上籃（兩分球，成功率 70%，但有 15% 機率被蓋火鍋）")
        
        choice = input("請輸入選擇 (1/2/3): ")
        
        print("\n🏀 球員運球尋找機會...", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")

        # 計算隨機機率 (1-100)
        chance = random.randint(1, 100)

        if choice == "1":
            print("🏀 你在罰球線附近急停跳投...")
            if chance <= 55:
                print("✨ 唰！空心入網！得到 2 分！")
                player_score += 2
            else:
                print("❌ 哐當！彈框而出，沒進！")
                
        elif choice == "2":
            print("🏀 你在三分線外後撤步，高高躍起，手起刀落...")
            if chance <= 35:
                print("🎉 哇！神射手！三分球進了！全場沸騰！")
                player_score += 3
            else:
                print("❌ 投得太大力了，打鐵！")
                
        elif choice == "3":
            print("🏀 你加速變向，強行切入禁區...")
            if chance <= 15:
                print("🚫 啪！對手中鋒賞了你一個大火鍋！球飛出界外！")
            elif chance <= 70:
                print("💪 頂著防守對抗上籃，球在籃框滾了兩圈...進了！得到 2 分！")
                player_score += 2
            else:
                print("❌ 失去平衡，上籃過力滾了出來！")
                
        else:
            print("⚠️ 緊張到運球出界！浪費了一次進攻機會！")

        # 每回合結束後，對手也會隨機得 0~2 分
        opponent_attack = random.choice([0, 0, 2])
        if opponent_attack == 2:
            print("😮 轉身過來，對手也透過快攻拿到了 2 分！")
            opponent_score += 2
        else:
            print("🛡️ 防守成功！對手這一波進攻沒進！")

        possessions -= 1
        print("=========================================\n")
        time.sleep(1)

    # 遊戲結局判斷
    print("🏁 逼—— 比赛結束！")
    print(f"最終比分 -> 你: {player_score} | 對手: {opponent_score}")
    
    if player_score > opponent_score:
        print("🏆 恭喜你！完成驚天逆轉，贏得了比賽的勝利！！！")
    elif player_score == opponent_score:
        print("🤝 雙方打平！比賽進入延長賽！")
    else:
        print("😭 很遺憾，逆轉失敗，下場比賽再接再厲！")

# 啟動遊戲
if __name__ == "__main__":
    basketball_game()
