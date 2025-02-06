import os
import numpy as np
import argparse

def process_folder(folder):
    """
    해당 폴더 내의 모든 .npz 파일을 처리하여,
    파일명과 평균 lddt 값을 리스트로 반환합니다.
    """
    results = []
    for file_name in os.listdir(folder):
        if file_name.endswith(".npz"):
            file_path = os.path.join(folder, file_name)
            try:
                data = np.load(file_path)
                if "lddt" in data:
                    lddt_values = data["lddt"]
                    average_lddt = np.mean(lddt_values)
                    results.append((file_name, average_lddt))
            except Exception as e:
                print(f"파일 {file_path}을(를) 처리하는 중 오류 발생: {e}")
    return results

def main():
    # Argument parser 설정
    parser = argparse.ArgumentParser(
        description="지정한 경로 내의 모든 서브폴더에서 npz 파일의 lddt 평균을 계산하여 폴더명_result.txt 파일로 저장합니다."
    )
    parser.add_argument("folder_path", type=str, help="최상위 폴더 경로")
    args = parser.parse_args()

    root_folder = args.folder_path

    if not os.path.isdir(root_folder):
        print("유효하지 않은 폴더 경로입니다.")
        return

    # os.walk를 사용하여 최상위 폴더 아래 모든 서브폴더를 재귀적으로 탐색
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # 현재 폴더에 npz 파일이 있는지 확인
        if any(f.endswith(".npz") for f in filenames):
            print(f"처리 중: {dirpath}")
            results = process_folder(dirpath)
            if results:
                # 현재 폴더의 이름을 기반으로 결과 파일 이름 지정 (예: 폴더명이 "sample"이면 sample_result.txt)
                folder_name = os.path.basename(os.path.normpath(dirpath))
                output_file = os.path.join(dirpath, f"{folder_name}_result.txt")
                with open(output_file, "w") as f:
                    # 파일명과 평균 lddt 값을 탭으로 구분하여 기록
                    for file_name, avg_lddt in results:
                        f.write(f"{file_name}\t{avg_lddt}\n")
                print(f"결과가 {output_file}에 저장되었습니다.")

if __name__ == "__main__":
    main()
