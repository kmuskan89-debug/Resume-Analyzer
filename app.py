"""
AI Resume Analyzer - Streamlit Frontend
A web application to analyze resumes against job descriptions
"""

import streamlit as st
from resume_extractor import (
    extract_text_from_pdf,
    extract_text_from_docx,
    clean_text,
    extract_skills,
    calculate_match_score,
    get_missing_skills,
    generate_suggestions,
    SKILLS_LIST,
    detect_job_role,
    get_role_required_skills,
    calculate_role_based_score,
    get_matched_skills_for_role,
    get_role_missing_skills,
    generate_role_recommendations
)

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Simple CSS for basic styling
st.markdown("""
    <style>
    .main-title { font-size: 2.5rem; font-weight: 800; text-align: center; color: blue; }
    .main-subtitle { text-align: center; color: white; font-size: 1.1rem; margin-bottom: 2rem; }
    .section-header { font-size: 1.3rem; font-weight: 700; color: #1e293b; margin: 20px 0 15px 0; }
    .score-display { background: linear-gradient(135deg, #6366f1, #8b5cf6); padding: 30px; border-radius: 15px; text-align: center; color: white; margin: 20px 0; }
    .score-value { font-size: 3.5rem; font-weight: bold; }
    .skill-tag { background: #e0e7ff; color: #3730a3; padding: 8px 14px; border-radius: 20px; margin: 4px; display: inline-block; font-weight: 600; }
    .skill-tag-missing { background: #fef3c7; color: #92400e; }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.markdown('<div class="main-title">📄 AI Resume Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Upload your resume and match it against job descriptions</div>', unsafe_allow_html=True)
    
    # Upload Section
    st.subheader("📎 Upload Your Resume")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=['pdf', 'docx'])
    
    if uploaded_file:
        file_icon = "📄" if uploaded_file.name.endswith('.pdf') else "📝"
        st.success(f"{file_icon} File uploaded: {uploaded_file.name}")
    
    # Job Description Section
    st.subheader("💼 Job Description")
    job_description = st.text_area("Paste the job description", height=150, placeholder="e.g., We are looking for a white hat hacker with experience in penetration testing...")
    
    if job_description:
        st.caption(f"📝 {len(job_description)} characters")
    
    # Analyze Button
    if st.button("🔍 Analyze Resume", type="primary", use_container_width=True):
        if uploaded_file is None:
            st.error("⚠️ Please upload a resume file first!")
        elif not job_description.strip():
            st.error("⚠️ Please enter a job description first!")
        else:
            with st.spinner("Analyzing your resume..."):
                try:
                    # Extract text
                    file_extension = uploaded_file.name.split('.')[-1].lower()
                    if file_extension == 'pdf':
                        resume_text = extract_text_from_pdf(uploaded_file)
                    elif file_extension == 'docx':
                        resume_text = extract_text_from_docx(uploaded_file)
                    else:
                        st.error("Unsupported file format!")
                        st.stop()
                    
                    resume_text = clean_text(resume_text)
                    resume_skills = extract_skills(resume_text)
                    job_skills = extract_skills(job_description)
                    
                    # Detect job role
                    detected_role, role_confidence = detect_job_role(job_description)
                    role_required_skills = []
                    role_missing_skills = []
                    
                    if detected_role:
                        role_required_skills = get_role_required_skills(detected_role)
                    
                    # Calculate scores
                    match_score = calculate_match_score(resume_text, job_description)
                    missing_skills = get_missing_skills(resume_skills, job_skills)
                    
                    # Use role-based skills if job_skills is empty
                    if not job_skills and detected_role and role_required_skills:
                        role_missing_skills = get_role_missing_skills(resume_skills, role_required_skills)
                        missing_skills = role_missing_skills
                    
                    suggestions = generate_suggestions(match_score, missing_skills)
                    
                    # Results
                    st.divider()
                    st.subheader("📊 Analysis Results")
                    
                    # Calculate progress value (0-1 range for Streamlit)
                    progress_value = min(match_score / 100, 1.0)
                    
                    # Score
                    if match_score >= 70:
                        st.success(f"🎉 Match Score: {match_score}% - Great Match!")
                    elif match_score >= 50:
                        st.warning(f"👍 Match Score: {match_score}% - Good Progress")
                    else:
                        st.error(f"📈 Match Score: {match_score}% - Needs Improvement")
                    
                    st.progress(progress_value)
                    
                    # Skills columns
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("### ✅ Your Skills")
                        if resume_skills:
                            for skill in resume_skills:
                                st.markdown(f'<span class="skill-tag">✓ {skill.title()}</span>', unsafe_allow_html=True)
                            st.caption(f"{len(resume_skills)} skills found")
                        else:
                            st.warning("No skills detected in resume")
                    
                    with col2:
                        st.markdown("### ❌ Missing Skills")
                        if missing_skills:
                            for skill in missing_skills:
                                st.markdown(f'<span class="skill-tag skill-tag-missing">✗ {skill.title()}</span>', unsafe_allow_html=True)
                            st.caption(f"{len(missing_skills)} skills to add")
                        else:
                            st.success("Perfect match! No missing skills")
                    
                    # Suggestions
                    st.subheader("💡 Suggestions")
                    for i, suggestion in enumerate(suggestions, 1):
                        st.info(f"**{i}.** {suggestion}")
                    
                    # Role-Based Analysis
                    if detected_role and role_required_skills:
                        st.divider()
                        st.subheader(f"🎯 Role-Based Analysis: {detected_role.title()}")
                        
                        role_score = calculate_role_based_score(resume_skills, role_required_skills)
                        role_matched_skills = get_matched_skills_for_role(resume_skills, role_required_skills)
                        role_missing_skills = get_role_missing_skills(resume_skills, role_required_skills)
                        recommendation = generate_role_recommendations(role_missing_skills, detected_role)
                        
                        if role_score >= 70:
                            st.success(f"🎉 Role Match: {role_score}% - Excellent!")
                        elif role_score >= 50:
                            st.warning(f"👍 Role Match: {role_score}% - Good")
                        else:
                            st.error(f"📈 Role Match: {role_score}% - Needs Work")
                        
                        # Calculate progress value (0-1 range for Streamlit)
                        role_progress_value = min(role_score / 100, 1.0)
                        st.progress(role_progress_value)
                        st.caption(f"Role detected with {role_confidence:.0f}% confidence")
                        
                        col_r1, col_r2 = st.columns(2)
                        
                        with col_r1:
                            st.markdown("#### ✅ Matched Skills")
                            if role_matched_skills:
                                for skill in role_matched_skills:
                                    st.markdown(f'<span class="skill-tag">✓ {skill.title()}</span>', unsafe_allow_html=True)
                            else:
                                st.warning("No matching skills found")
                        
                        with col_r2:
                            st.markdown("#### ❌ Missing Skills")
                            if role_missing_skills:
                                for skill in role_missing_skills:
                                    st.markdown(f'<span class="skill-tag skill-tag-missing">✗ {skill.title()}</span>', unsafe_allow_html=True)
                            else:
                                st.success("All required skills found!")
                        
                        st.subheader("📌 Recommendation")
                        st.warning(f"💡 **{recommendation}**")
                    
                    st.balloons()
                    st.success("🎉 Analysis complete! Good luck with your job search!")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.warning("Please try again with a different file.")


if __name__ == "__main__":
    main()

