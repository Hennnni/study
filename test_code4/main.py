import os
from pill_detector import detect_pills
from remove_bg import crop_and_save_objects
from pill_classifier import load_resnet_model, classify_pills

if __name__ == "__main__":
    # 경로 설정
    yolo_model_path = '../models/yolov8/best.pt'
    source_image_path = '../data/test_img/029760_029667_028134_028127.jpg'
    save_project_path = '../data/test_results'
    resnet_model_path = '../models/resnet/ResNet50_0614_bs64_e100.keras'

    class_labels = ['K-028463', 'K-028460', 'K-023740', 'K-023599', 'K-021644', 'K-028763', 'K-031544', 'K-028635', 'K-021325', 'K-027049', 'K-028161', 'K-034237', 'K-027059', 'K-021264', 'K-028450', 'K-028134', 'K-028466', 'K-034321', 'K-034093', 'K-032550', 'K-023085', 'K-027840', 'K-032270', 'K-028465', 'K-021270', 'K-032583', 'K-027735', 'K-034095', 'K-023807', 'K-029667', 'K-031701', 'K-028828', 'K-028145', 'K-032303', 'K-028146', 'K-028864', 'K-027053', 'K-028442', 'K-027693', 'K-032377', 'K-027048', 'K-023779', 'K-028813', 'K-023208', 'K-028130', 'K-028122', 'K-028345', 'K-032410', 'K-028516', 'K-028074', 'K-021731', 'K-023425', 'K-022846', 'K-032341', 'K-034215', 'K-031695', 'K-031391', 'K-028137', 'K-028641', 'K-031328', 'K-028128', 'K-023357', 'K-034505', 'K-034316', 'K-028555', 'K-028509', 'K-032342', 'K-023544', 'K-028709', 'K-031327', 'K-027052', 'K-032575', 'K-027816', 'K-028693', 'K-027076', 'K-028296', 'K-023594', 'K-023092', 'K-034356', 'K-031472', 'K-028814', 'K-028010', 'K-028360', 'K-032562', 'K-027815', 'K-028482', 'K-034297', 'K-032541', 'K-028740', 'K-021063', 'K-028385', 'K-028790', 'K-029534', 'K-028336', 'K-021062', 'K-034503', 'K-023612', 'K-028495', 'K-032441', 'K-034502', 'K-032440', 'K-023804', 'K-032579', 'K-034501', 'K-028081', 'K-032544', 'K-034264', 'K-028258', 'K-027733', 'K-027077', 'K-031330', 'K-028716', 'K-023424', 'K-023957', 'K-021387', 'K-031753', 'K-027070', 'K-023829', 'K-021733', 'K-000609', 'K-028129', 'K-027338', 'K-021652', 'K-034249', 'K-021683', 'K-031490', 'K-027039', 'K-028127', 'K-028481', 'K-031481', 'K-032567', 'K-028359', 'K-028232', 'K-031302', 'K-032580', 'K-029760', 'K-028144', 'K-032543', 'K-023084', 'K-032561', 'K-032505', 'K-028493', 'K-034275', 'K-034251', 'K-027057', 'K-034142', 'K-031702', 'K-021266', 'K-026794', 'K-028475', 'K-024162', 'K-032521', 'K-028210', 'K-027046', 'K-027060', 'K-023252', 'K-032403', 'K-031624', 'K-027064', 'K-034250', 'K-028468', 'K-028076', 'K-031705', 'K-028684', 'K-027073', 'K-027055', 'K-031680', 'K-028354', 'K-031326', 'K-021612', 'K-032597', 'K-021692', 'K-034091', 'K-021268', 'K-031699', 'K-027978', 'K-028155', 'K-021260', 'K-023838', 'K-028209', 'K-021553', 'K-032615', 'K-001029', 'K-032448', 'K-032591', 'K-021732', 'K-023729', 'K-027068', 'K-032493', 'K-021065', 'K-021555', 'K-027040', 'K-032600', 'K-029533', 'K-032537', 'K-028469', 'K-034285', 'K-034448', 'K-031473', 'K-026813', 'K-028683', 'K-027061', 'K-032442', 'K-021351', 'K-031494', 'K-028121', 'K-028792', 'K-027078', 'K-034192', 'K-028334', 'K-032547', 'K-024631', 'K-028208', 'K-003078', 'K-028073', 'K-004637']
    
    print("Step 1: YOLO 감지 시작")
    results, image_name = detect_pills(yolo_model_path, source_image_path, save_project_path)
    print(f"Step 1: YOLO 감지 완료 - 이미지 이름: {image_name}")
    
    print("Step 2: 배경 제거 및 객체 저장 시작")
    label_file_path = f'../data/test_results/{image_name}/labels/{image_name}.txt'
    output_dir = f'../output/rembg_img/{image_name}/'
    crop_and_save_objects(source_image_path, label_file_path, output_dir)
    print("Step 2: 배경 제거 및 객체 저장 완료")

    print("Step 3: ResNet 분류 시작")
    resnet_model = load_resnet_model(resnet_model_path)
    print("Step 3: ResNet 모델 로드 완료")

    classify_pills(resnet_model, output_dir, class_labels)
    print("Step 3: ResNet 분류 완료")
