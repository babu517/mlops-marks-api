# 🎓 MLOps Marks Prediction API

Live API: https://mlops-marks-api.onrender.com

Predicts whether a student passes or fails based on marks.

## 🚀 Live Demo

- Home: https://mlops-marks-api.onrender.com/
- Predict Pass (55): https://mlops-marks-api.onrender.com/predict?marks=55
- Predict Fail (30): https://mlops-marks-api.onrender.com/predict?marks=30
- API Docs: https://mlops-marks-api.onrender.com/docs

## 📊 Logic

- Marks >= 40 → Pass (1)
- Marks < 40 → Fail (0)

```json
{
  "marks": 55,
  "pass": 1
}

🛠️ Tech StackPython + FastAPIDockerGitHubRender (Cloud Deployment + Auto Redeploy)

Run Locally
pip install -r requirements.txt
uvicorn app:app --reload

Open: http://localhost:8000/predict?marks=55🔄 MLOps Workflow

Build API with FastAPIDockerizePush to GitHubAuto-deploy on RenderFix bug → Push → Auto-redeploy → Verify Live

AuthorBuilt as part of MLOps learning journey.

