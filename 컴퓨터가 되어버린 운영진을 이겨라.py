import random

class Player:
    def __init__(self,name):
        self.name = name
        self.card = None
        self.score = 0
        self.round_wins = 0
        
    def __str__(self):
        return f"{self.name}"
    
    def select_card(self):
        return 0
        
    
class Game:
    def __init__(self, players: list[str]):
        self.players = players
        self.you : Player = None
        self.computers : list[Player] = []
        
    def start_game(self): # 여기서 캐릭터를 선택하도록 하자. 메인 실행 함수 설정
        # print("Game start!")
        your_index = int(input("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4): ")) - 1
        self.you = Player(self.players[your_index])
        self.computers = [Player(player) for player in self.players if player != self.players[your_index]]
        for round in range(1,5):
            self.play_round(round, self.you, *self.computers)
        # self.game_result()
            
    def play_round(self, round, you, *computers): # 라운드 시작할때마다 덱을 생성해야겠지? 그리고 카드를 뽑아야할듯
        print("===========================")
        print(f"     ROUND {round} - START")
        print("===========================")
        play_list: list[Player] = self.set_play_order(round, you, *computers)
        print(f"게임은 {', '.join(str(player) for player in play_list)} 순으로 진행됩니다.\n")
        # card_deck = [random.randint(1, 13) for _ in range(30)]
        return 0
    
    def set_play_order(self, round, you, *computers): # 첫라운드는 이름순, 그 후는 점수가 낮은 순서대로 카드를 뽑는다.
        players: list[Player] = [*computers]
        players.append(you)
        if round == 1:
            ascending_order = sorted(players, key=lambda x : x.name) # 객체인데... 객체안의 name순서로 정렬을 할수는 없을까... lambda을 이용하면 되는구나
            return ascending_order
        else:
            score_order = sorted(players, key=lambda x : x.score)
            return score_order
    
    def play_game(self): # 각 플레이어가 카드를 가지고. 게임을 시작한다
        return 0
    
    def game_result(self):
        return 0
        

if __name__ == '__main__':
    players=["박신빈", "윤정원", "임담희", "김용현"]
    game = Game(players) 
    game.start_game()