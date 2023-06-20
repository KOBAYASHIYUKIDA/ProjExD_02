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

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    bd_img = pg.Surface((20, 20))  # 直径20の正方形
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)  # 空のsurfaceの中心座標
    bd_img.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rect = bd_img.get_rect() # 爆弾Surface (bd_img)から爆弾Rect (bd_rect)を抽出
    bd_rect.center = x, y  # 爆弾の中心座標を乱数で表示
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rect.move_ip(sum_mv)
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        bd_rect.move_ip(vx, vy)
        screen.blit(bd_img, bd_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()