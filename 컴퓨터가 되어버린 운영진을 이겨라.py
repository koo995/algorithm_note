import random

class Player:
    def __init__(self,name):
        self.name = name
        self.card = None
        self.score = 0
        self.round_wins = 0
        
    def __str__(self):
        return f"{self.name}"
    
    def select_card(self, deck: list[str]):
        self.card = deck.pop()        
    
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
            self.play_round(round, self.you, self.computers)
        self.game_result(self.you, self.computers)
            
    def play_round(self, round, you, computers:list[Player]): # 라운드 시작할때마다 덱을 생성해야겠지? 그리고 카드를 뽑아야할듯
        print("===========================")
        print(f"     ROUND {round} - START")
        print("===========================")
        play_list: list[Player] = self.set_play_order(round, you, computers)
        # deck을 생성
        card_deck = [random.randint(1, 13) for _ in range(30)]
        # print(" 만들어진 deck: ", card_deck)
        print(f"게임은 {', '.join(str(player) for player in play_list)} 순으로 진행됩니다.\n")
        self.play_game(play_list, card_deck)
        self.round_result(round, play_list)
    
    def set_play_order(self, round, you:Player, computers: list[Player]): # 첫라운드는 이름순, 그 후는 점수가 낮은 순서대로 카드를 뽑는다.
        players = [*computers] # 언패킹후 다시 리스트로 감싸준다.
        players.append(you)
        if round == 1:
            ascending_order = sorted(players, key=lambda x:x.name) # 객체인데... 객체안의 name순서로 정렬을 할수는 없을까... lambda을 이용하면 되는구나
            return ascending_order
        else:
            score_order = sorted(players, key=lambda x:x.score, reverse=True)
            return score_order
    
    def play_game(self, play_list:list[Player], deck): # 각 플레이어가 카드를 가지고. 게임을 시작한다
        # 먼저 플레이어들에게 card을 줘야겠어
        print("===========플레이어가 뽑은 카드============")
        for player in play_list:
            player.select_card(deck)
            # print(" 현재 deck 상태:", deck)
            print(f">> {player.name}  (현재 점수: {player.score})")
            print(f">> 뽑은 카드: {player.card} \n")
        winners = self.get_winners(play_list)
        self.set_score(winners, play_list)
        
    def set_score(self, winners:list[Player], players:list[Player]):
        max_card = winners[0].card
        min_card = min(players, key=lambda x:x.card).card
        score_offset = max_card - min_card
        for winner in winners:
            winner.score += score_offset
            winner.round_wins += 1
            print(f">>>> {winner.name}님이 {score_offset}점을 얻었습니다 \\^_^/ <<<<")
         
    
    def get_winners(self, players):
        # 승자가 여러명일 수 있잖아? 어케하지? 제일 큰 카드를 가진 녀석들을 리스트에 담는다?
        winners = []
        max_card = -int(1e9)
        for player in players:
            if max_card == player.card:
                winners.append(player)
            if max_card < player.card:
                winners.clear()
                max_card = player.card
                winners.append(player)
        return winners
                
    
    def round_result(self, round, players):
        print("===========================")
        print(f"     ROUND {round} - END")
        print("===========================")
        for i, player in enumerate(players, start=1):
            print(f"{i}. {player} : {player.score}점")
        print()
        
    def game_result(self, you, computers):
        players = [*computers]
        players.append(you)
        print("=============================")
        print("     게임 순위 - 점수")
        print("=============================")
        players.sort(key=lambda x:x.score, reverse=True)
        for i, player in enumerate(players, start=1):
            if player != you:
                print(f"{i}등 - {player.name} : {player.score}점")
            else:
                print(f"{i}등 - *{player.name}* : {player.score}점")
        print("=============================")
        print("     게임 순위 - 승리 횟수")
        print("=============================")
        players.sort(key=lambda x:x.round_wins, reverse=True)
        for i, player in enumerate(players, start=1):
            if player != you:
                print(f"{i}등 - {player.name} : {player.round_wins}점")
            else:
                print(f"{i}등 - *{player.name}* : {player.round_wins}점")


if __name__ == '__main__':
    players=["박신빈", "윤정원", "임담희", "김용현"]
    game = Game(players) 
    game.start_game()
    
# card_deck이 코드 전체에서 reference로 작동하네? 이거 지역변수면 그렇게 안되는 거 아닌가...
# 함수의 지역변수는 함수가 실행되는 동안에만 존재한다. 각 함수가 호출되어 실행될 때 만들어지고, 함수의 실행이 끝나면 모두 삭제된다.
# 반대의 케이스도 고려해 봐야겠는데? 새로운 변수로써 생성되는 경우는 어케함? 
# 매개변수로 안받고 똑같은 이름을 짓고 처리할려고 하면 reference가 아니고 새롭게 생성되는구나