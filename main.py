from automator import Automator
from target import TargetType

if __name__ == '__main__':
    # 声明货物要移动到的建筑 ID 。
    targets = {
        # TargetType.Chair: 1,
        # TargetType.Box: 2,
        # TargetType.Dogfood: 2,
        # TargetType.Sofa: 3,
        # TargetType.Plant: 3,
        TargetType.Microphone: 4,
        # TargetType.Shoes: 5,
        TargetType.Chicken: 5,
        # TargetType.Bottle: 4,
        # TargetType.Vegetable: 5,
        # TargetType.Food: 8,
        # TargetType.Book: 5,
        # TargetType.Bag: 6,
        # TargetType.Wood: 7,
        TargetType.Coal: 8,
        TargetType.Oil: 9,
        # # TargetType.Food: 8,
        # TargetType.Iron: 8,
        # TargetType.Grass:9,
        TargetType.Tool: 7,
        # TargetType.Quilt: 9,
    }

    # 连接 adb ，MuMu 模拟器默认 adb 控制链接为 127.0.0.1:7555 。
    instance = Automator('ba3a606e', targets)

    # 启动脚本。
    instance.start()
