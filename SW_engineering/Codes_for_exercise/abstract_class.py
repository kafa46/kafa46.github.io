
from abc import ABCMeta, abstractmethod

class AbstractRemocon(metaclass=ABCMeta):
    
    def __init__(self, TV_id):
        self.TV_id = TV_id
    
    # 일반 메서드
    def show_welcome_msg(self,):
        print(f'안녕하세요, CJU전자 {self.TV_id} 리모콘 입니다.')
    
    # 추상 메서드 1
    @abstractmethod
    def television_on(self,):
        pass
    
    # 추상 메서드 2
    @abstractmethod
    def television_off(self,):
        pass


class LowEndTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')


class HieghEndTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')

        
class PremiumTVRemocon(AbstractRemocon):
    
    def __init__(self, TV_id):
        super().__init__(TV_id)   
    
    # 추상 메서드 오버라이딩
    def television_on(self,):
        print('전원을 켭니다.')    
    
    # 추상 메서드 오버라이딩
    def television_off(self,):
        print('전원을 끕니다.')
    
    # 고급형 TV 추가 기능
    def connect_Netflix(self,):
        print('넷플릭스에 연결합니다.')
    
    # 프리미엄 TV 추가 기능
    def start_voice_AI(self,):
        print('음성인식 기능을 시작합니다.')
        
        
if __name__=='__main__':
    low_end_tv = LowEndTVRemocon('일반형TV_001')
    low_end_tv.show_welcome_msg()
    low_end_tv.television_on()
    low_end_tv.television_off()
    
    high_end_tv = HieghEndTVRemocon('고급형TV_002')
    high_end_tv.show_welcome_msg()
    high_end_tv.television_on()
    high_end_tv.television_off()
    high_end_tv.connect_Netflix()
    
    premium_tv = PremiumTVRemocon('프리미엄TV_003')
    premium_tv.show_welcome_msg()
    premium_tv.television_on()
    premium_tv.television_off()
    premium_tv.connect_Netflix()
    premium_tv.start_voice_AI()