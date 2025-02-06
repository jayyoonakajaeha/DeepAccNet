#!/bin/bash
# run_all.sh
# ~/BM55 폴더 내의 각 서브폴더에 대해 DeepAccNet-noPyRosetta.py 스크립트를 실행합니다.

# 기본 폴더 설정 (필요에 따라 경로 수정)
BASE_DIR=~/BM55
OUTPUT_DIR=outputs

# 출력 디렉토리가 없으면 생성합니다.
mkdir -p "$OUTPUT_DIR"

# BASE_DIR 내의 모든 항목에 대해 반복합니다.
for subdir in "$BASE_DIR"/*; do
    # 항목이 디렉토리인 경우에만 실행
    if [ -d "$subdir" ]; then
        # 서브폴더 이름 추출
        subdirname=$(basename "$subdir")
        echo "Processing $subdirname ..."
        
        # 스크립트 실행
        python DeepAccNet-noPyRosetta.py -r -v "$subdir" "$OUTPUT_DIR/$subdirname"
    fi
done
