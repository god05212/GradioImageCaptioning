# GradioImageCaptioning  
## 이미지 설명 AI  
**프로젝트 기간:** 2025/08/20(수)  
<br/>

## 개요  
이 프로젝트는 Gradio 인터페이스와 Hugging Face의 Transformers 라이브러리를 활용하여, **이미지를 입력하면 해당 이미지에 대한 설명(캡션)을 자동으로 생성**해주는 AI 기반 웹 데모입니다.  
최근 비전-언어 통합 모델의 발전으로, 이미지 속 정보를 자연어로 설명하는 기술(Image Captioning)이 주목받고 있으며, 이는 **시각장애인 보조, 이미지 검색 최적화, 자동 콘텐츠 생성** 등 다양한 분야에서 활용되고 있습니다.  

본 프로젝트는 이러한 기술을 **Gradio 웹 서비스 형태로 구현**하여, **간단한 웹 기반 인터페이스를 통해 누구나 쉽게 AI 이미지 설명 서비스를 체험**할 수 있도록 설계되었습니다.  
> Gradio는 완전한 웹 프레임워크는 아니지만, 머신러닝 모델을 손쉽게 웹에서 시연할 수 있도록 해주는 경량화된 **웹 애플리케이션 형태의 인터페이스**를 제공합니다.

<br/>

## 프로젝트 목표  
이미지를 업로드하면 AI가 이미지 내용을 분석하여 **자연어로 설명을 생성하는 웹 인터페이스**를 구축합니다.  
<br/>

## 사용 기술  
- **AI 모델**: Hugging Face Transformers  
  - 기본 모델: `Salesforce/blip-image-captioning-base`  
  - 대체 모델: `nlpconnect/vit-gpt2-image-captioning`  
- **웹 인터페이스**: Gradio  
- **이미지 처리**: PIL (Python Imaging Library)  
- **기타 도구**: Python, pip, `device_map="auto"`로 GPU 자동 할당  
<br/>

## 구현 기능  
1. **Gradio 기반 인터페이스 구현**  
   - 웹 브라우저에서 이미지 업로드 및 설명 결과 확인  
2. **이미지 설명 생성 기능**  
   - 업로드된 이미지에 대해 AI 모델이 자동으로 설명 생성  
3. **다양한 모델 지원 및 예외 처리**  
   - 기본적으로 BLIP 모델 사용, 오류 발생 시 다른 경량 모델로 대체  
4. **오류 대응 처리**  
   - 이미지 미입력 또는 예외 발생 시 사용자 친화적 메시지 출력  
5. **실시간 웹 공유**  
   - Gradio의 `share=True` 기능으로 외부 사용자에게도 즉시 공유  
<br/>

## 프로젝트 수행 과정  
1. **모델 로딩**  
   - `transformers.pipeline("image-to-text")`로 BLIP 모델 로딩  
   - 시스템 환경에 따라 `device_map="auto"`로 자동 자원 할당  
   - 로드 실패 시 대체 모델 자동 사용  

2. **이미지 분석 함수 작성**  
   - Gradio로 업로드된 PIL 이미지를 텍스트 설명으로 변환  

3. **Gradio UI 구성**  
   - 입력: 이미지 업로드 필드  
   - 출력: 생성된 텍스트 설명  
   - 부가 설명 텍스트 포함  

4. **웹 애플리케이션 실행**  
   - `iface.launch(share=True)` 실행  
   - 고유 URL 발급으로 외부 사용자 접속 가능  
<br/>

## 사용한 모델  
### Hugging Face Image Captioning 모델  
- **기본 모델**: `Salesforce/blip-image-captioning-base`  
- **대체 모델**: `nlpconnect/vit-gpt2-image-captioning`  

**특징**  
- 이미지 내 주요 요소와 장면을 자연스러운 문장으로 설명  
- 단일 이미지 입력만으로 복잡한 추론 가능  
- GPU 또는 CPU 환경 자동 최적화  
- BLIP: Vision-Language Pretraining 기반의 고성능 모델  
<br/>

## 기존 사이트와 차이점  
- **Transformer 기반 이미지 설명 기능의 웹 통합**  
  - 단순 이미지 처리 아닌, AI 기반 이미지-텍스트 생성 기능 통합  

- **모델 예외 처리 자동화**  
  - BLIP 모델 실패 시 자동 대체 모델로 전환  

- **빠른 배포 및 접근성 향상**  
  - Gradio의 `share=True` 설정으로 누구나 손쉽게 접속 가능  
<br/>

## 향후 추가할 수 있는 기능  
- **멀티 이미지 입력 지원**  
  - 여러 이미지 업로드 및 각각 설명 출력  

- **설명 결과 음성 출력 (TTS)**  
  - 텍스트 설명을 음성으로 변환해 **시각장애인 보조 기능 강화**  

- **사용자 피드백 기능 연동**  
  - 생성된 설명에 대한 '좋아요 / 싫어요' 등의 반응 수집  

- **다국어 번역 기능 추가**  
  - 생성된 설명을 한국어/영어 등 다양한 언어로 자동 번역  
<br/>

![image](https://github.com/user-attachments/assets/4654b8be-fc81-4148-9886-4dbbb4ce0078)
