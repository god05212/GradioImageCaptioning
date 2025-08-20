import gradio as gr
from transformers import pipeline
from PIL import Image

# Image-to-Text 파이프라인 초기화 (BLIP 모델 사용)
# 더 작은 모델을 사용하거나 device_map="auto"를 사용하면 메모리 제약을 줄일 수 있습니다.
try:
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base", device_map="auto")
except Exception as e:
    print(f"모델 로드 중 오류 발생: {e}")
    print("더 작은 모델로 시도합니다: nlpconnect/vit-gpt2-image-captioning")
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning", device_map="auto")


def analyze_image(image):
    if image is None:
        return "이미지를 업로드해주세요."
    try:
        # PIL Image 객체를 모델에 전달
        text_description = image_to_text(image)[0]['generated_text']
        return f"이미지 설명: {text_description}"
    except Exception as e:
        return f"이미지 분석 중 오류 발생: {e}"

# Gradio 인터페이스 설정
iface = gr.Interface(
    fn=analyze_image,
    inputs=gr.Image(type="pil", label="이미지 업로드"), # PIL Image 객체로 받도록 설정
    outputs="text",
    title="📸 이미지 설명 AI 챗봇",
    description="이미지를 업로드하시면 AI가 이미지 내용을 설명해 드립니다."
)

# Gradio 앱 실행
iface.launch(share=True)
