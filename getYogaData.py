
import json
import requests

raw_branchData =requests.get('https://goodtime.17fit.com/branch-list')
formatted_branchData = json.dumps(raw_branchData.json(), indent=2, ensure_ascii=False)



def getFilterClassData(branchId,page,date,view):

    params = {
    'date': date,
    'view_type':view,
    'page': page,
    'only_recently': '1',
    'load_over_recently': '0',
    'today_class_service_provider_id': '',
}
    
    raw_classData = requests.get(f'https://17fit.com/webapi/branch-class-schedule/{branchId}',params=params)

    if raw_classData.status_code == 200:
    # 使用json.dumps格式化JSON數據,確保使用雙引號
        formatted_json = json.dumps(raw_classData.json(), indent=2, ensure_ascii=False)
        
        return formatted_json
    else:
        return (f"請求失敗，狀態: {raw_classData.status_code}")

