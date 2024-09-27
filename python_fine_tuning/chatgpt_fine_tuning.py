from openai import OpenAI
api_key = ""
client = OpenAI(api_key=api_key)
#第一步
# result = client.files.create(
#   file=open("test.jsonl", "rb"),
#   purpose="fine-tune"
# )
# print(result)


#第二步
# client.fine_tuning.jobs.create(
#   training_file="file-Qql2cFkqKBNGQkTGCBHn6tZq", #把第一步print(result)裡的id貼過來 
#   model="gpt-4o-mini-2024-07-18",#models取一個來fine-tuning
  # model="gpt-4o-2024-08-06"
  # model="gpt-3.5-turbo"
#   hyperparameters={
#     "n_epochs":5
#   }
# )

#觀看訓練進度
  # 列出10個微調
# client.fine_tuning.jobs.list(limit=10)

# 檢視微調狀態
# client.fine_tuning.jobs.retrieve("file-NgJU3uCaXpe6vB7YLrJy27QD")

  #取消微調
# client.fine_tuning.jobs.cancel("file-NgJU3uCaXpe6vB7YLrJy27QD")

  # 列出微調作業中最多的10個
# client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-abc123", limit=10)

  # 刪除微調模型
# client.models.delete("ft:gpt-3.5-turbo-0125:personal::9w59o39j")

#model
#ft:gpt-3.5-turbo-0125:personal::9z4t441Q