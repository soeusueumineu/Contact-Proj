class Friend:
    def __init__(self, name, p_num, address):
        self.name = name
        self.p_num = p_num
        self.address = address

    def all_show_data(self):
        print(f"이름: {self.name}")
        print(f"전화: {self.p_num}")
        print(f"주소: {self.address}")

    def basic_show_data(self):
        pass

    def update_info(self, name=None, p_num=None, address=None):
        if name:
            self.name = name
        if p_num:
            self.p_num = p_num
        if address:
            self.address = address


class HighFriend(Friend):
    def __init__(self, name, p_num, address, job):
        super().__init__(name, p_num, address)
        self.job = job

    def all_show_data(self):
        super().all_show_data()
        print(f"직업: {self.job}")
        print("")

    def basic_show_data(self):
        print(f"이름: {self.name}")
        print(f"전화: {self.p_num}")
        print("")

    def update_info(self, job=None, **kwargs):
        super().update_info(**kwargs)
        if job:
            self.job = job


class UnivFriend(Friend):
    def __init__(self, name, p_num, address, major):
        super().__init__(name, p_num, address)
        self.major = major

    def all_show_data(self):
        super().all_show_data()
        print(f"전공: {self.major}")
        print("")

    def basic_show_data(self):
        print(f"이름: {self.name}")
        print(f"전화: {self.p_num}")
        print(f"전공: {self.major}")
        print("")

    def update_info(self, major=None, **kwargs):
        super().update_info(**kwargs)
        if major:
            self.major = major


class FriendInfoController:
    def __init__(self, num):
        self.my_friends = [None] * num
        self.number_of_friends = 0

    def add_friend(self, choice):
        name = input("이름: ")
        p_num = input("전화: ")
        address = input("주소: ")

        if choice == 1:
            job = input("직업: ")
            friend = HighFriend(name, p_num, address, job)
        elif choice == 2:
            major = input("학과: ")
            friend = UnivFriend(name, p_num, address, major)

        self.my_friends[self.number_of_friends] = friend
        self.number_of_friends += 1
        print("입력 완료!")

    def all_show_data(self):
        for i in range(self.number_of_friends):
            self.my_friends[i].all_show_data()
            print("")  

    def basic_show_data(self):
        for i in range(self.number_of_friends):
            self.my_friends[i].basic_show_data()
            print("")
            
    def update_friend(self):
        name = input("수정할 친구의 이름: ")
        friend = self.search_friend_by_name(name)
        if friend:
            new_name = input("새 이름 (없으면 Enter): ")
            new_p_num = input("새 전화 (없으면 Enter): ")
            new_address = input("새 주소 (없으면 Enter): ")
            if isinstance(friend, HighFriend):
                new_job = input("새 직업 (없으면 Enter): ")
                friend.update_info(name=new_name, p_num=new_p_num, address=new_address, job=new_job)
            elif isinstance(friend, UnivFriend):
                new_major = input("새 전공 (없으면 Enter): ")
                friend.update_info(name=new_name, p_num=new_p_num, address=new_address, major=new_major)
            print("정보가 업데이트되었습니다.")
        else:
            print("친구를 찾을 수 없습니다.")

    def delete_friend(self):
        name = input("삭제할 친구의 이름: ")
        for i in range(self.number_of_friends):
            if self.my_friends[i] and self.my_friends[i].name == name:
                del self.my_friends[i]
                self.my_friends.append(None)
                self.number_of_friends -= 1
                print("친구가 삭제되었습니다.")
                return
        print("친구를 찾을 수 없습니다.")

    def search_friend(self):
        name = input("검색할 친구의 이름: ")
        friend = self.search_friend_by_name(name)
        if friend:
            friend.all_show_data()
        else:
            print("친구를 찾을 수 없습니다.")

    def search_friend_by_name(self, name):
        for friend in self.my_friends:
            if friend and friend.name == name:
                return friend
        return None


def main():
    controller = FriendInfoController(10)

    while True:
        print(" ")
        print("*** 메뉴 선택 ***")
        print("1. 고교 친구 정보 저장")
        print("2. 대학 친구 정보 저장")
        print("3. 전체 정보 출력")
        print("4. 기본 정보 출력")
        print("5. 정보 수정")
        print("6. 정보 삭제")
        print("7. 사람 검색")
        print("8. 프로그램 종료")
        choice = int(input("선택>> "))

        if choice == 1 or choice == 2:
            controller.add_friend(choice)
        elif choice == 3:
            controller.all_show_data()
        elif choice == 4:
            controller.basic_show_data()
        elif choice == 5:
            controller.update_friend()
        elif choice == 6:
            controller.delete_friend()
        elif choice == 7:
            controller.search_friend()
        elif choice == 8:
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
