import subprocess

# 列表包含所有要處理的影片路徑
videos = [

    # "/004/edit_video/004L_sa_1_split/004L_sa_1_1.mp4",
    # "/004/edit_video/004L_sa_1_split/004L_sa_1_2.mp4",
    # "/004/edit_video/004L_sa_1_split/004L_sa_1_3.mp4",
    # "/004/edit_video/004L_sa_1_split/004L_sa_1_4.mp4",
    # "/004/edit_video/004L_sa_1_split/004L_sa_1_5.mp4",

    # "/004/edit_video/004L_sa_2_split/004L_sa_2_1.mp4",
    # "/004/edit_video/004L_sa_2_split/004L_sa_2_2.mp4",
    # "/004/edit_video/004L_sa_2_split/004L_sa_2_3.mp4",
    # "/004/edit_video/004L_sa_2_split/004L_sa_2_4.mp4",
    # "/004/edit_video/004L_sa_2_split/004L_sa_2_5.mp4",

    # "/004/edit_video/004L_sb_1_split/004L_sb_1_1.mp4",
    # "/004/edit_video/004L_sb_1_split/004L_sb_1_2.mp4",
    # "/004/edit_video/004L_sb_1_split/004L_sb_1_3.mp4",
    # "/004/edit_video/004L_sb_1_split/004L_sb_1_4.mp4",
    # "/004/edit_video/004L_sb_1_split/004L_sb_1_5.mp4",

    # "/004/edit_video/004L_sb_2_split/004L_sb_2_1.mp4",
    # "/004/edit_video/004L_sb_2_split/004L_sb_2_2.mp4",
    # "/004/edit_video/004L_sb_2_split/004L_sb_2_3.mp4",
    # "/004/edit_video/004L_sb_2_split/004L_sb_2_4.mp4",
    # "/004/edit_video/004L_sb_2_split/004L_sb_2_5.mp4",

    # "/004/edit_video/004R_ha_1_split/004R_ha_1_1.mp4",
    # "/004/edit_video/004R_ha_1_split/004R_ha_1_2.mp4",
    # "/004/edit_video/004R_ha_1_split/004R_ha_1_3.mp4",
    # "/004/edit_video/004R_ha_1_split/004R_ha_1_4.mp4",
    # "/004/edit_video/004R_ha_1_split/004R_ha_1_5.mp4",

    # "/004/edit_video/004R_ha_2_split/004R_ha_2_1.mp4",
    # "/004/edit_video/004R_ha_2_split/004R_ha_2_2.mp4",
    # "/004/edit_video/004R_ha_2_split/004R_ha_2_3.mp4",
    # "/004/edit_video/004R_ha_2_split/004R_ha_2_4.mp4",
    # "/004/edit_video/004R_ha_2_split/004R_ha_2_5.mp4",

    # "/004/edit_video/004R_hb_1_split/004R_hb_1_1.mp4",
    # "/004/edit_video/004R_hb_1_split/004R_hb_1_2.mp4",
    # "/004/edit_video/004R_hb_1_split/004R_hb_1_3.mp4",
    # "/004/edit_video/004R_hb_1_split/004R_hb_1_4.mp4",
    # "/004/edit_video/004R_hb_1_split/004R_hb_1_5.mp4",

    # "/004/edit_video/004R_hb_2_split/004R_hb_2_1.mp4",
    # "/004/edit_video/004R_hb_2_split/004R_hb_2_2.mp4",
    # "/004/edit_video/004R_hb_2_split/004R_hb_2_3.mp4",
    # "/004/edit_video/004R_hb_2_split/004R_hb_2_4.mp4",
    # "/004/edit_video/004R_hb_2_split/004R_hb_2_5.mp4",

    # #################################################

    # "/005/edit_video/005L_sa_1_split/005L_sa_1_1.mp4",
    # "/005/edit_video/005L_sa_1_split/005L_sa_1_2.mp4",
    # "/005/edit_video/005L_sa_1_split/005L_sa_1_3.mp4",
    # "/005/edit_video/005L_sa_1_split/005L_sa_1_4.mp4",
    # "/005/edit_video/005L_sa_1_split/005L_sa_1_5.mp4",
    # "/005/edit_video/005L_sa_1_split/005L_sa_1_6.mp4",

    # "/005/edit_video/005L_sa_2_split/005L_sa_2_1.mp4",
    # "/005/edit_video/005L_sa_2_split/005L_sa_2_2.mp4",
    # "/005/edit_video/005L_sa_2_split/005L_sa_2_3.mp4",
    # "/005/edit_video/005L_sa_2_split/005L_sa_2_4.mp4",
    # "/005/edit_video/005L_sa_2_split/005L_sa_2_5.mp4",
    # "/005/edit_video/005L_sa_2_split/005L_sa_2_6.mp4",

    # "/005/edit_video/005L_sb_1_split/005L_sb_1_1.mp4",
    # "/005/edit_video/005L_sb_1_split/005L_sb_1_2.mp4",
    # "/005/edit_video/005L_sb_1_split/005L_sb_1_3.mp4",
    # "/005/edit_video/005L_sb_1_split/005L_sb_1_4.mp4",
    # "/005/edit_video/005L_sb_1_split/005L_sb_1_5.mp4",
    # "/005/edit_video/005L_sb_1_split/005L_sb_1_6.mp4",

    # "/005/edit_video/005L_sb_2_split/005L_sb_2_1.mp4",
    # "/005/edit_video/005L_sb_2_split/005L_sb_2_2.mp4",
    # "/005/edit_video/005L_sb_2_split/005L_sb_2_3.mp4",
    # "/005/edit_video/005L_sb_2_split/005L_sb_2_4.mp4",
    # "/005/edit_video/005L_sb_2_split/005L_sb_2_5.mp4",
    # "/005/edit_video/005L_sb_2_split/005L_sb_2_6.mp4",

    # "/005/edit_video/005R_ha_1_split/005R_ha_1_1.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_2.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_3.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_4.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_5.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_6.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_7.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_8.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_9.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_10.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_11.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_12.mp4",
    # "/005/edit_video/005R_ha_1_split/005R_ha_1_13.mp4",

    # "/005/edit_video/005R_ha_2_split/005R_ha_2_1.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_2.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_3.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_4.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_5.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_6.mp4",
    # "/005/edit_video/005R_ha_2_split/005R_ha_2_7.mp4",

    # "/005/edit_video/005R_hb_1_split/005R_hb_1_1.mp4",
    # "/005/edit_video/005R_hb_1_split/005R_hb_1_2.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_3.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_4.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_5.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_6.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_7.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_8.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_9.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_10.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_11.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_12.mp4",
    "/005/edit_video/005R_hb_1_split/005R_hb_1_13.mp4",

    "/005/edit_video/005R_hb_2_split/005R_hb_2_1.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_2.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_3.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_4.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_5.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_6.mp4",
    "/005/edit_video/005R_hb_2_split/005R_hb_2_7.mp4",

]

# 迴圈遍歷每個影片並執行命令
for video in videos:
    print(f'current video path: {video}')
    command = ["python", "demo/vis.py", "--video", video]
    subprocess.run(command)


# python batch_process.py

