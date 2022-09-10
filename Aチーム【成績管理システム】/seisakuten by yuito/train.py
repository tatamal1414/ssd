from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import numpy as np
import os
import glob

names =["abe","arata", "ayano","chiba","fujiwara","fukuyama","oguri","suda","takeuchi","tamaki","aragaki","ayase",
        "fukada", "hamabe", "hashimoto", "hirose", "ishihara", "nagano", "nagasawa", "toda"]
abe = []
ayano =[]
chiba =[]
fujiwara =[]
fukuyama =[]
arata =[]
oguri = []
suda = []
takeuchi = []
tamaki = []
aragaki = []
ayase = []
fukada = []
hamabe = []
hashimoto = []
hirose = []
ishihara = []
nagano = []
nagasawa = []
toda = []

#### MTCNN ResNet のモデル読み込み
mtcnn = MTCNN()
resnet = InceptionResnetV1(pretrained='vggface2').eval()

#### 画像ファイルから画像の特徴ベクトルを取得(ndarray 512次元)
def feature_vector(image_path):
    img = Image.open(image_path)
    img_cropped = mtcnn(img)
    feature_vector = resnet(img_cropped.unsqueeze(0))
    feature_vector_np = feature_vector.squeeze().to('cpu').detach().numpy().copy()
    return feature_vector_np

#### 2つのベクトル間のコサイン類似度を取得(cosine_similarity(a, b) = a・b / |a||b|)
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#### 2枚の画像からそれぞれの特徴ベクトルを取得
for i in range(len(names)):
    for j, path in enumerate(glob.glob(f"./Face2/{names[i]}/*.jpg")):
        # 被写体の写真path
        img1_fv = feature_vector("./Face2/abe/cutted1.jpg")
        # 芸能人の写真path
        img2_fv = feature_vector(path)
        similarity = float(cosine_similarity(img1_fv, img2_fv))
        if i == 0:
            abe.append(similarity)
        elif i == 1:
            arata.append(similarity)
        elif i == 2:
            ayano.append(similarity)
        elif i == 3:
            chiba.append(similarity)
        elif i == 4:
            fujiwara.append(similarity)
        elif i == 5:
            fukuyama.append(similarity)
        elif i == 6:
            oguri.append(similarity)
        elif i == 7:
            suda.append(similarity)
        elif i == 8:
            takeuchi.append(similarity)
        elif i == 9:
            tamaki.append(similarity)
        elif i == 10:
            aragaki.append(similarity)
        elif i == 11:
            ayase.append(similarity)
        elif i == 12:
            fukada.append(similarity)
        elif i == 13:
            hamabe.append(similarity)
        elif i == 14:
            hashimoto.append(similarity)
        elif i == 15:
            hirose.append(similarity)
        elif i == 16:
            ishihara.append(similarity)
        elif i == 17:
            nagano.append(similarity)
        elif i == 18:
            nagasawa.append(similarity)
        else:
            toda.append(similarity)

result = {"阿部寛": max(abe), "新田真剣佑": max(arata), "綾野剛": max(ayano), "千葉雄大": max(chiba),
            "藤原竜也": max(fujiwara), "福山雅治": max(fukuyama), "小栗旬": max(oguri),
             "菅田将暉": max(suda), "竹内涼真": max(takeuchi), "玉木宏": max(tamaki), "新垣結衣": max(aragaki),
             "綾瀬はるか": max(ayase), "深田恭子": max(fukada), "浜辺美波": max(hamabe), "橋本環奈": max(hashimoto),
              "広瀬すず": max(hirose), "石原さとみ": max(ishihara), "永野芽郁": max(nagano), "長澤まさみ": max(nagasawa),
              "戸田恵梨香": max(toda)}
print(max(zip(result.values(),result.keys())))
# (glob.glob(f"./Face2/{name}/*.jpg"))
#### 2枚の画像間の類似度を取得

