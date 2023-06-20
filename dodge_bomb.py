import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

def check_bound(rect: pg.Rect) -> tuple[bool, bool]:
    """
    画面外、画面内を判定する関数
    引数：kk_rect or bd_rect
    戻り値：横方向、縦方向の判定結果タプル（True；画面内、False：画面外）
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    # こうかとんの向き画像 追加機能 1 未実装
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_RIGHT_UP = [kk_img, pg.transform.rotozoom(kk_img, 45, 1.0)]
    kk_img_UP = [kk_img, pg.transform.rotozoom(kk_img, 90, 1.0)]
    kk_img_LEFT = pg.transform.flip(kk_img, True, False)
    kk_img_LEFT_UP = [kk_img_LEFT, pg.transform.rotozoom(kk_img_LEFT, 315, 1.0)]  # こうかとんの画像を315度回転させました。
    kk_img_LEFT_DOWN = [kk_img_LEFT, pg.transform.rotozoom(kk_img_LEFT, 45, 1.0)]  # こうかとんの画像を45度回転させました。
    kk_img_DOWN = [kk_img, pg.transform.rotozoom(kk_img, 270, 1.0)]
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    bd_img = pg.Surface((20, 20))  # 直径20の正方形 練習1
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)  # 空のsurfaceの中心座標
    bd_img.set_colorkey((0, 0, 0)) # 黒い部分の透明化
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rect = bd_img.get_rect() # 爆弾Surface (bd_img)から爆弾Rect (bd_rect)を抽出
    bd_rect.center = x, y  # 爆弾の中心座標を乱数で表示
    vx, vy = +5, +5  # 練習2

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0])
        if kk_rect.colliderect(bd_rect):  # 練習5
            kk_img = pg.image.load("ex02/fig/8.png") # 追加機能3
            kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
            screen.blit(kk_img, kk_rect) 
            pg.display.update() 
            clock.tick(0.2) 
            print("ゲームオーバー")
            return   # ゲームオーバー 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rect.move_ip(sum_mv)
        if check_bound(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(kk_img, kk_rect)
        bd_rect.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rect)
        if not yoko:  # 横方向に画面外だったら
            vx *= -1
        if not tate:  # 縦方向に範囲外だったら
            vy *= -1
        screen.blit(bd_img, bd_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()