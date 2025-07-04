import os
import xml.etree.ElementTree as ET

def extract_question_and_answer(base_path):
    

    #add all folders 
    folders =[
        "1_CancerGov_QA",
        "2_GARD_QA",
        "3_GHR_QA",
        "4_MPlus_Health_Topics_QA",
        "5_NIDDK_QA",
        "6_NINDS_QA",
        "7_SeniorHealth_QA",
        "8_NHLBI_QA_XML",
        "9_CDC_QA",
        "10_MPlus_ADAM_QA",
        "11_MPlusDrugs_QA",
        "12_MPlusHerbsSupplements_QA",
    ]

    qa_entries=[]

    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            continue

        for filename in os.listdir(folder_path):
            if filename.endswith(".xml"):
                file_path = os.path.join(folder_path, filename)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    qa_pairs = root.find("QAPairs")
                    if qa_pairs:
                        for qa in qa_pairs.findall("QAPair"):
                            question = qa.findtext("Question")
                            answer = qa.findtext("Answer")
                            if question and answer:
                                qa_entries.append({"question": question.strip(), "answer": answer.strip()})
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")

    print(f"✅ Total QA pairs loaded: {len(qa_entries)}")
    return qa_entries
