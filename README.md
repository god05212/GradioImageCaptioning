# gradio_image_captioning
## 예측모델 기반 Image Captioning 웹서비스
프로젝트 기간: 2025/08/20(수)
<br/>

## 개요
이 프로젝트는 Gradio 인터페이스와 Hugging Face의 Transformers 라이브러리를 활용하여, 이미지를 입력하면 해당 이미지에 대한 설명(캡션)을 자동으로 생성해주는 웹 기반 AI 애플리케이션입니다.
최근 비전-언어 통합 모델의 발전으로, 이미지 속 정보를 자연어로 설명하는 기술(Image Captioning)이 주목받고 있으며, 이는 시각장애인 보조, 이미지 검색 최적화, 자동 콘텐츠 생성 등 다양한 분야에서 활용되고 있습니다.
본 프로젝트는 이러한 기술을 Gradio 웹서비스에 통합함으로써, 간단한 웹 인터페이스를 통해 누구나 쉽게 AI 이미지 설명 서비스를 체험할 수 있도록 설계되었습니다.

프로젝트 목표
이미지를 업로드하면 AI가 이미지 내용을 분석하여 자연어로 설명을 생성하는 웹 애플리케이션을 구축합니다.
<br/>

사용 기술

AI 모델: Hugging Face Transformers (Salesforce/blip-image-captioning-base, 대체: vit-gpt2-image-captioning)

웹 인터페이스: Gradio

이미지 처리: PIL (Python Imaging Library)

기타 도구: Python, pip, device_map="auto"로 GPU 자동 할당

<br/>
구현 기능

Gradio 기반 인터페이스 구현

웹 브라우저에서 이미지 업로드 및 설명 결과 확인 가능

이미지 설명 생성 기능

업로드된 이미지에 대해 AI 모델이 자동으로 설명 생성

다양한 모델 지원 및 예외 처리

기본적으로 BLIP 모델 사용, 오류 발생 시 다른 경량 모델로 대체

오류 대응 처리

이미지가 없거나 예외 발생 시 사용자 친화적 메시지 반환

실시간 웹 공유

Gradio의 share=True 기능으로 외부 사용자에게도 즉시 공개

<br/>
프로젝트 수행 과정

사전 학습된 이미지 캡셔닝 모델 로딩

Hugging Face transformers.pipeline을 통해 BLIP 모델 로딩

시스템 환경에 따라 device_map="auto"로 GPU/CPU 자동 매핑

모델 로드 실패 시 대체 모델(vit-gpt2-image-captioning) 자동 사용

이미지 분석 함수 작성

Gradio에서 PIL 이미지를 받아 텍스트 설명 생성

결과를 텍스트 형태로 사용자에게 반환

Gradio UI 구성

입력: 이미지 업로드 필드

출력: 생성된 이미지 설명 텍스트

제목 및 간단한 설명 추가

웹 애플리케이션 실행

iface.launch(share=True)를 통해 웹에서 앱 실행

고유 URL 생성으로 외부 사용자도 접속 가능

<br/>
사용한 모델
Hugging Face Image Captioning 모델

본 프로젝트에서는 Hugging Face의 pipeline("image-to-text") 기능을 사용하여, BLIP 기반 사전학습 모델을 활용해 이미지로부터 텍스트 설명을 생성하였습니다.

기본 모델: Salesforce/blip-image-captioning-base

대체 모델: nlpconnect/vit-gpt2-image-captioning

특징

이미지 내 주요 요소와 장면을 이해하여 자연스러운 문장으로 설명 생성

단일 이미지 입력만으로도 복잡한 추론 가능

GPU 또는 CPU 환경에 따라 자동 최적화 실행

BLIP은 Vision-Language Pretraining을 기반으로 고성능 이미지 캡션 결과 제공

<br/>
기존 사이트와 차이점

AI 이미지 설명 기능의 웹 통합
OpenCV나 단순 이미지 처리 기능이 아닌, Transformer 기반 이미지-텍스트 모델을 실제 웹에서 실시간으로 활용

예외 상황에 강한 모델 구성
모델 로드 실패 시 자동으로 대체 모델을 사용하는 로직 구성

빠른 배포 및 접근성 향상
Gradio의 간단한 설정만으로 누구나 웹에서 AI 기능 체험 가능

<br/>
향후 추가할 수 있는 기능

멀티 이미지 입력 지원
한 번에 여러 이미지를 업로드하고 각각 설명 출력

설명 결과 음성 출력(TTS)
이미지 설명을 자동 음성으로 변환해 시각장애인 보조 기능 추가

사용자 피드백 기능 연동
사용자가 생성된 설명에 대한 피드백(좋아요/싫어요 등) 제공

다국어 번역 기능 연계
생성된 설명을 한국어/영어 등 다양한 언어로 자동 번역

https://huggingface.co/spaces/god05212/ImageTalkBot
