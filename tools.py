from typing import List, Dict, Any
from langchain.tools import tool
import requests
import os
import json
import random
import datetime

@tool
def Recruitment_Agent() -> List[Dict[str, Any]]:
    """
    Return all function definitions for the Recruitment Agent.
    """
    funcs: List[Dict[str, Any]] = []
    
    funcs.append({
        "agent": "Recruitment",
        "function": "make_candidate_sourcing_workflow",
        "required_fields": ['job_title'],
        "optional_fields": ['location', 'experience_level', 'skills', 'channels'],
        "permissions": "read",
        "description": "Execute make candidate sourcing workflow operation in Recruitment.",
        "keywords": ['make', 'candidate', 'sourcing', 'workflow'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "make_candidate_screening_workflow",
        "required_fields": ['candidate_name'],
        "optional_fields": ['resume_url', 'job_requirements'],
        "permissions": "read",
        "description": "Execute make candidate screening workflow operation in Recruitment.",
        "keywords": ['make', 'candidate', 'screening', 'workflow'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "make_onboarding_workflow",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['department'],
        "permissions": "read",
        "description": "Execute make onboarding workflow operation in Recruitment.",
        "keywords": ['make', 'onboarding', 'workflow'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "asana_get_recruitment_projects",
        "required_fields": [],
        "optional_fields": ['team_gid', 'job_title', 'limit'],
        "permissions": "read",
        "description": "Execute asana get recruitment projects operation in Recruitment.",
        "keywords": ['asana', 'get', 'recruitment', 'projects'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "asana_create_interview_task",
        "required_fields": ['candidate_name', 'interview_type', 'interview_date', 'project_gid'],
        "optional_fields": ['interviewer_gid', 'due_date', 'notes'],
        "permissions": "write",
        "description": "Execute asana create interview task operation in Recruitment.",
        "keywords": ['asana', 'create', 'interview', 'task'],
        "requires_connector": True,
        "verbs": ['create', 'add'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "asana_create_onboarding_tasks",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['project_gid', 'assignee_gid'],
        "permissions": "write",
        "description": "Execute asana create onboarding tasks operation in Recruitment.",
        "keywords": ['asana', 'create', 'onboarding', 'tasks'],
        "requires_connector": True,
        "verbs": ['create', 'add'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })

    funcs.append({
        "agent": "Recruitment",
        "function": "docusign_send_offer_letter",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['salary', 'template_id'],
        "permissions": "write",
        "description": "Execute docusign send offer letter operation in Recruitment.",
        "keywords": ['docusign', 'send', 'offer', 'letter'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "docusign_get_envelope_status",
        "required_fields": ['envelope_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Execute docusign get envelope status operation in Recruitment.",
        "keywords": ['docusign', 'get', 'envelope', 'status'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "docusign_send_onboarding_documents",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['document_types'],
        "permissions": "write",
        "description": "Execute docusign send onboarding documents operation in Recruitment.",
        "keywords": ['docusign', 'send', 'onboarding', 'documents'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "yousign_send_offer_letter",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['salary'],
        "permissions": "write",
        "description": "Execute yousign send offer letter operation in Recruitment.",
        "keywords": ['yousign', 'send', 'offer', 'letter'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "yousign_get_signature_status",
        "required_fields": ['signature_request_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Execute yousign get signature status operation in Recruitment.",
        "keywords": ['yousign', 'get', 'signature', 'status'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "yousign_send_onboarding_documents",
        "required_fields": ['candidate_name', 'candidate_email', 'job_title', 'start_date'],
        "optional_fields": ['document_types'],
        "permissions": "write",
        "description": "Execute yousign send onboarding documents operation in Recruitment.",
        "keywords": ['yousign', 'send', 'onboarding', 'documents'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "la_bonne_boite_search_companies",
        "required_fields": ['job_title', 'location'],
        "optional_fields": ['rome_code', 'limit'],
        "permissions": "read",
        "description": "Execute la bonne boite search companies operation in Recruitment.",
        "keywords": ['la', 'bonne', 'boite', 'search', 'companies'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "la_bonne_boite_get_company_details",
        "required_fields": ['siret'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Execute la bonne boite get company details operation in Recruitment.",
        "keywords": ['la', 'bonne', 'boite', 'get', 'company', 'details'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "la_bonne_boite_get_hiring_insights",
        "required_fields": ['job_title', 'location'],
        "optional_fields": ['rome_code'],
        "permissions": "read",
        "description": "Execute la bonne boite get hiring insights operation in Recruitment.",
        "keywords": ['la', 'bonne', 'boite', 'get', 'hiring', 'insights'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "hellowork_search_candidates",
        "required_fields": ['job_title'],
        "optional_fields": ['location', 'experience_level', 'limit'],
        "permissions": "read",
        "description": "Execute hellowork search candidates operation in Recruitment.",
        "keywords": ['hellowork', 'search', 'candidates'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "hellowork_post_job",
        "required_fields": ['job_title', 'job_description', 'location'],
        "optional_fields": ['contract_type', 'salary'],
        "permissions": "write",
        "description": "Execute hellowork post job operation in Recruitment.",
        "keywords": ['hellowork', 'post', 'job'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "hellowork_get_applications",
        "required_fields": ['job_id'],
        "optional_fields": ['status', 'limit'],
        "permissions": "read",
        "description": "Execute hellowork get applications operation in Recruitment.",
        "keywords": ['hellowork', 'get', 'applications'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "rome_search_job_codes",
        "required_fields": ['job_title'],
        "optional_fields": ['limit'],
        "permissions": "read",
        "description": "Execute rome search job codes operation in Recruitment.",
        "keywords": ['rome', 'search', 'job', 'codes'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "rome_get_code_details",
        "required_fields": ['rome_code'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Execute rome get code details operation in Recruitment.",
        "keywords": ['rome', 'get', 'code', 'details'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "rome_match_job_to_candidate",
        "required_fields": ['job_rome_code', 'candidate_skills'],
        "optional_fields": ['candidate_experience'],
        "permissions": "read",
        "description": "Execute rome match job to candidate operation in Recruitment.",
        "keywords": ['rome', 'match', 'job', 'to', 'candidate'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "linkedin_recruiter_search_candidates",
        "required_fields": ['job_title'],
        "optional_fields": ['location', 'experience_level', 'skills', 'limit'],
        "permissions": "read",
        "description": "Execute linkedin recruiter search candidates operation in Recruitment.",
        "keywords": ['linkedin', 'recruiter', 'search', 'candidates'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "linkedin_recruiter_send_inmail",
        "required_fields": ['profile_id', 'candidate_name', 'message_subject', 'message_body'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Execute linkedin recruiter send inmail operation in Recruitment.",
        "keywords": ['linkedin', 'recruiter', 'send', 'inmail'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "linkedin_recruiter_get_candidate_profile",
        "required_fields": ['profile_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Execute linkedin recruiter get candidate profile operation in Recruitment.",
        "keywords": ['linkedin', 'recruiter', 'get', 'candidate', 'profile'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "smartrecruiters_create_job",
        "required_fields": ['job_title', 'job_description', 'location'],
        "optional_fields": ['department', 'employment_type'],
        "permissions": "write",
        "description": "Post and publish a job listing to SmartRecruiters ATS system.",
        "keywords": ['smartrecruiters', 'post', 'publish', 'job', 'listing', 'posting'],
        "requires_connector": True,
        "verbs": ['post', 'publish', 'create', 'add'],
        "produces": ['job_posting', 'job_listing'],
        "consumes": ['job_title', 'job_description', 'location'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "smartrecruiters_get_candidates",
        "required_fields": [],
        "optional_fields": ['job_id', 'status', 'limit'],
        "permissions": "read",
        "description": "Execute smartrecruiters get candidates operation in Recruitment.",
        "keywords": ['smartrecruiters', 'get', 'candidates'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Recruitment",
        "function": "smartrecruiters_schedule_interview",
        "required_fields": ['candidate_id', 'job_id', 'interview_type', 'interview_date'],
        "optional_fields": ['interviewer_email', 'location'],
        "permissions": "read",
        "description": "Execute smartrecruiters schedule interview operation in Recruitment.",
        "keywords": ['smartrecruiters', 'schedule', 'interview'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],

        "status": "active"
    })
    
    return funcs

@tool
def Content_Agent() -> List[Dict[str, Any]]:
    """
    Return all function definitions for the Content Agent.
    """
    funcs: List[Dict[str, Any]] = []
    
    # Fireflies.ai
    funcs.append({
        "agent": "Content",
        "function": "fireflies_generate_content_from_transcript",
        "required_fields": ['transcript_id', 'content_type'],
        "optional_fields": ['tone', 'length', 'format'],
        "permissions": "read",
        "description": "Generate content from a Fireflies.ai transcript.",
        "keywords": ['fireflies', 'generate', 'content', 'transcript'],
        "requires_connector": True,
        "verbs": ['generate', 'create'],
        "produces": ['generated_content'],
        "consumes": ['transcript_id', 'content_type'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "fireflies_extract_content_insights",
        "required_fields": ['transcript_id'],
        "optional_fields": ['keywords', 'topics'],
        "permissions": "read",
        "description": "Extract insights from a Fireflies.ai transcript.",
        "keywords": ['fireflies', 'extract', 'insights', 'transcript'],
        "requires_connector": True,
        "verbs": ['extract', 'analyze'],
        "produces": ['insights'],
        "consumes": ['transcript_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "fireflies_format_content_for_channel",
        "required_fields": ['content', 'channel'],
        "optional_fields": ['formatting_rules'],
        "permissions": "read",
        "description": "Format content for a specific channel using Fireflies.ai data.",
        "keywords": ['fireflies', 'format', 'content', 'channel'],
        "requires_connector": True,
        "verbs": ['format', 'process'],
        "produces": ['formatted_content'],
        "consumes": ['content', 'channel'],
        "status": "active"
    })
    
    # Slack
    funcs.append({
        "agent": "Content",
        "function": "slack_post_formatted_content",
        "required_fields": ['channel_id', 'content'],
        "optional_fields": ['thread_ts', 'attachments'],
        "permissions": "write",
        "description": "Post formatted content to a Slack channel.",
        "keywords": ['slack', 'post', 'content', 'message'],
        "requires_connector": True,
        "verbs": ['post', 'send'],
        "produces": ['message_ts'],
        "consumes": ['channel_id', 'content'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "slack_create_content_thread",
        "required_fields": ['channel_id', 'initial_content'],
        "optional_fields": ['replies'],
        "permissions": "write",
        "description": "Create a content thread in Slack.",
        "keywords": ['slack', 'create', 'thread', 'content'],
        "requires_connector": True,
        "verbs": ['create', 'start'],
        "produces": ['thread_ts'],
        "consumes": ['channel_id', 'initial_content'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "slack_schedule_content_post",
        "required_fields": ['channel_id', 'content', 'post_at'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Schedule a content post in Slack.",
        "keywords": ['slack', 'schedule', 'post', 'content'],
        "requires_connector": True,
        "verbs": ['schedule', 'plan'],
        "produces": ['scheduled_message_id'],
        "consumes": ['channel_id', 'content', 'post_at'],
        "status": "active"
    })
    
    # Power Automate
    funcs.append({
        "agent": "Content",
        "function": "power_automate_trigger_content_distribution",
        "required_fields": ['flow_id', 'content_payload'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Trigger a content distribution flow in Power Automate.",
        "keywords": ['power', 'automate', 'trigger', 'distribution'],
        "requires_connector": True,
        "verbs": ['trigger', 'start'],
        "produces": ['run_id'],
        "consumes": ['flow_id', 'content_payload'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "power_automate_create_content_workflow",
        "required_fields": ['workflow_name', 'triggers', 'actions'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Create a content workflow in Power Automate.",
        "keywords": ['power', 'automate', 'create', 'workflow'],
        "requires_connector": True,
        "verbs": ['create', 'build'],
        "produces": ['workflow_id'],
        "consumes": ['workflow_name', 'triggers', 'actions'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "power_automate_format_and_distribute_content",
        "required_fields": ['content', 'channels'],
        "optional_fields": ['formatting_options'],
        "permissions": "write",
        "description": "Format and distribute content via Power Automate.",
        "keywords": ['power', 'automate', 'format', 'distribute'],
        "requires_connector": True,
        "verbs": ['format', 'distribute'],
        "produces": ['distribution_status'],
        "consumes": ['content', 'channels'],
        "status": "active"
    })
    
    # Notion
    funcs.append({
        "agent": "Content",
        "function": "notion_create_formatted_content_page",
        "required_fields": ['parent_page_id', 'title', 'content_blocks'],
        "optional_fields": ['cover_image', 'icon'],
        "permissions": "write",
        "description": "Create a formatted content page in Notion.",
        "keywords": ['notion', 'create', 'page', 'content'],
        "requires_connector": True,
        "verbs": ['create', 'add'],
        "produces": ['page_id', 'page_url'],
        "consumes": ['parent_page_id', 'title', 'content_blocks'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "notion_update_content_page",
        "required_fields": ['page_id'],
        "optional_fields": ['title', 'content_blocks', 'properties'],
        "permissions": "write",
        "description": "Update a content page in Notion.",
        "keywords": ['notion', 'update', 'page', 'content'],
        "requires_connector": True,
        "verbs": ['update', 'edit'],
        "produces": ['page_id'],
        "consumes": ['page_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "notion_format_content_for_export",
        "required_fields": ['page_id', 'export_format'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Format Notion content for export.",
        "keywords": ['notion', 'format', 'export', 'content'],
        "requires_connector": True,
        "verbs": ['format', 'export'],
        "produces": ['exported_content'],
        "consumes": ['page_id', 'export_format'],
        "status": "active"
    })
    
    # Synthesia
    funcs.append({
        "agent": "Content",
        "function": "synthesia_generate_video_script",
        "required_fields": ['topic', 'audience'],
        "optional_fields": ['tone', 'length'],
        "permissions": "read",
        "description": "Generate a video script for Synthesia.",
        "keywords": ['synthesia', 'generate', 'script', 'video'],
        "requires_connector": True,
        "verbs": ['generate', 'create'],
        "produces": ['script'],
        "consumes": ['topic', 'audience'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "synthesia_get_video_metadata",
        "required_fields": ['video_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get metadata for a Synthesia video.",
        "keywords": ['synthesia', 'get', 'metadata', 'video'],
        "requires_connector": True,
        "verbs": ['get', 'fetch'],
        "produces": ['video_metadata'],
        "consumes": ['video_id'],
        "status": "active"
    })
    
    # Canva
    funcs.append({
        "agent": "Content",
        "function": "canva_generate_design_specification",
        "required_fields": ['design_type', 'content_requirements'],
        "optional_fields": ['branding_guidelines'],
        "permissions": "read",
        "description": "Generate a design specification for Canva.",
        "keywords": ['canva', 'generate', 'design', 'spec'],
        "requires_connector": True,
        "verbs": ['generate', 'create'],
        "produces": ['design_spec'],
        "consumes": ['design_type', 'content_requirements'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "canva_get_design_metadata",
        "required_fields": ['design_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get metadata for a Canva design.",
        "keywords": ['canva', 'get', 'metadata', 'design'],
        "requires_connector": True,
        "verbs": ['get', 'fetch'],
        "produces": ['design_metadata'],
        "consumes": ['design_id'],
        "status": "active"
    })
    
    # SEMrush
    funcs.append({
        "agent": "Content",
        "function": "semrush_analyze_keywords",
        "required_fields": ['keywords', 'database'],
        "optional_fields": ['limit'],
        "permissions": "read",
        "description": "Analyze keywords using SEMrush.",
        "keywords": ['semrush', 'analyze', 'keywords', 'seo'],
        "requires_connector": True,
        "verbs": ['analyze', 'research'],
        "produces": ['keyword_analysis'],
        "consumes": ['keywords', 'database'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "semrush_analyze_content_seo",
        "required_fields": ['url', 'target_keywords'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Analyze content SEO using SEMrush.",
        "keywords": ['semrush', 'analyze', 'content', 'seo'],
        "requires_connector": True,
        "verbs": ['analyze', 'audit'],
        "produces": ['seo_analysis'],
        "consumes": ['url', 'target_keywords'],
        "status": "active"
    })
    
    # Buffer
    funcs.append({
        "agent": "Content",
        "function": "buffer_create_scheduled_post",
        "required_fields": ['profile_ids', 'text'],
        "optional_fields": ['media', 'scheduled_at', 'now'],
        "permissions": "write",
        "description": "Create a scheduled post in Buffer.",
        "keywords": ['buffer', 'create', 'scheduled', 'post'],
        "requires_connector": True,
        "verbs": ['create', 'schedule'],
        "produces": ['update_id'],
        "consumes": ['profile_ids', 'text'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Content",
        "function": "buffer_get_post_analytics",
        "required_fields": ['update_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get analytics for a Buffer post.",
        "keywords": ['buffer', 'get', 'analytics', 'post'],
        "requires_connector": True,
        "verbs": ['get', 'fetch'],
        "produces": ['analytics'],
        "consumes": ['update_id'],
        "status": "active"
    })
    
    return funcs


@tool
def Support_Agent() -> List[Dict[str, Any]]:
    """
    Return all function definitions for the Support Agent.
    """
    funcs: List[Dict[str, Any]] = []
    
    funcs.append({
        "agent": "Support",
        "function": "typeform_create_form",
        "required_fields": ['title', 'fields'],
        "optional_fields": ['workspace_id'],
        "permissions": "write",
        "description": "Create a new form in Typeform.",
        "keywords": ['typeform', 'create', 'form'],
        "requires_connector": True,
        "verbs": ['create', 'add'],
        "produces": ['form_id', 'form_url'],
        "consumes": ['title', 'fields'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "typeform_get_responses",
        "required_fields": ['form_id'],
        "optional_fields": ['since', 'until', 'limit'],
        "permissions": "read",
        "description": "Get responses for a Typeform form.",
        "keywords": ['typeform', 'get', 'responses'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve'],
        "produces": ['responses'],
        "consumes": ['form_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "typeform_analyze_nps_responses",
        "required_fields": ['form_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Analyze NPS responses from a Typeform form.",
        "keywords": ['typeform', 'analyze', 'nps', 'responses'],
        "requires_connector": True,
        "verbs": ['analyze', 'process'],
        "produces": ['nps_analysis'],
        "consumes": ['form_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "jira_service_management_create_request",
        "required_fields": ['service_desk_id', 'request_type_id', 'request_field_values'],
        "optional_fields": ['raise_on_behalf_of', 'request_participants'],
        "permissions": "write",
        "description": "Create a new request in Jira Service Management.",
        "keywords": ['jira', 'service', 'management', 'create', 'request'],
        "requires_connector": True,
        "verbs": ['create', 'add'],
        "produces": ['request_key', 'request_id'],
        "consumes": ['service_desk_id', 'request_type_id', 'request_field_values'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "jira_service_management_get_requests",
        "required_fields": [],
        "optional_fields": ['service_desk_id', 'request_status', 'search_term', 'start', 'limit'],
        "permissions": "read",
        "description": "Get requests from Jira Service Management.",
        "keywords": ['jira', 'service', 'management', 'get', 'requests'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve'],
        "produces": ['requests_list'],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "jira_service_management_update_request",
        "description": "Execute jira service management update request operation in Support.",
        "keywords": ['jira', 'service', 'management', 'update', 'request'],
        "requires_connector": True,
        "verbs": ['update', 'edit'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "jira_service_management_get_sla_status",
        "required_fields": [],
        "optional_fields": ['request_key', 'sla_breach_only'],
        "permissions": "read",
        "description": "Execute jira service management get sla status operation in Support.",
        "keywords": ['jira', 'service', 'management', 'get', 'sla', 'status'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    # WhatsApp Business API
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_send_message",
        "required_fields": ['phone_number', 'message'],
        "optional_fields": ['message_type', 'media_url', 'template_name'],
        "permissions": "write",
        "description": "Execute whatsapp business send message operation in Support.",
        "keywords": ['whatsapp', 'business', 'send', 'message'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_send_notification",
        "required_fields": ['phone_number', 'notification_type'],
        "optional_fields": ['template_data'],
        "permissions": "write",
        "description": "Execute whatsapp business send notification operation in Support.",
        "keywords": ['whatsapp', 'business', 'send', 'notification'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_get_messages",
        "required_fields": [],
        "optional_fields": ['phone_number', 'since', 'limit'],
        "permissions": "read",
        "description": "Execute whatsapp business get messages operation in Support.",
        "keywords": ['whatsapp', 'business', 'get', 'messages'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_analyze_conversation",
        "required_fields": ['phone_number'],
        "optional_fields": ['summarize'],
        "permissions": "read",
        "description": "Execute whatsapp business analyze conversation operation in Support.",
        "keywords": ['whatsapp', 'business', 'analyze', 'conversation'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    return funcs
    
@tool
def Crm_Agent() -> List[Dict[str, Any]]:
    """
    Return all function definitions for the CRM Agent.
    """
    funcs: List[Dict[str, Any]] = []
    
    funcs.append({
        "agent": "CRM",
        "function": "insee_get_company_by_siret",
        "required_fields": ['siret'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get company details by SIRET from INSEE SIRENE v3.",
        "keywords": ['insee', 'sirene', 'get', 'company', 'siret'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve'],
        "produces": ['company_details'],
        "consumes": ['siret'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "insee_search_companies_by_name",
        "required_fields": ['name'],
        "optional_fields": ['postal_code', 'city', 'limit'],
        "permissions": "read",
        "description": "Search companies by name from INSEE SIRENE v3.",
        "keywords": ['insee', 'sirene', 'search', 'companies', 'name'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": ['companies_list'],
        "consumes": ['name'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "insee_enrich_lead_with_company_data",
        "required_fields": ['lead_id', 'siret'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Enrich a lead with company data from INSEE SIRENE v3.",
        "keywords": ['insee', 'sirene', 'enrich', 'lead', 'company', 'data'],
        "requires_connector": True,
        "verbs": ['enrich', 'update'],
        "produces": ['enriched_lead'],
        "consumes": ['lead_id', 'siret'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "linkedin_sales_navigator_search_prospects",
        "required_fields": ['keywords'],
        "optional_fields": ['location', 'industry', 'title', 'company', 'limit'],
        "permissions": "read",
        "description": "Search for prospects using LinkedIn Sales Navigator.",
        "keywords": ['linkedin', 'sales', 'navigator', 'search', 'prospects'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": ['prospects_list'],
        "consumes": ['keywords'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "linkedin_sales_navigator_enrich_lead",
        "required_fields": ['lead_id', 'profile_url'],
        "optional_fields": [],
        "permissions": "write",
        "description": "Enrich a lead with data from LinkedIn Sales Navigator.",
        "keywords": ['linkedin', 'sales', 'navigator', 'enrich', 'lead'],
        "requires_connector": True,
        "verbs": ['enrich', 'update'],
        "produces": ['enriched_lead'],
        "consumes": ['lead_id', 'profile_url'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "linkedin_sales_navigator_get_company_insights",
        "required_fields": ['company_id'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get company insights from LinkedIn Sales Navigator.",
        "keywords": ['linkedin', 'sales', 'navigator', 'get', 'company', 'insights'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve'],
        "produces": ['company_insights'],
        "consumes": ['company_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "dropcontact_find_email",
        "required_fields": ['first_name', 'last_name', 'company'],
        "optional_fields": ['website'],
        "permissions": "read",
        "description": "Find email address for a contact using Dropcontact.",
        "keywords": ['dropcontact', 'find', 'email'],
        "requires_connector": True,
        "verbs": ['find', 'search', 'get'],
        "produces": ['email_address'],
        "consumes": ['first_name', 'last_name', 'company'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "dropcontact_enrich_contact",
        "required_fields": ['contact_id'],
        "optional_fields": ['email', 'linkedin_url'],
        "permissions": "write",
        "description": "Enrich a contact with data from Dropcontact.",
        "keywords": ['dropcontact', 'enrich', 'contact'],
        "requires_connector": True,
        "verbs": ['enrich', 'update'],
        "produces": ['enriched_contact'],
        "consumes": ['contact_id'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "dropcontact_verify_email",
        "required_fields": ['email'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Verify an email address using Dropcontact.",
        "keywords": ['dropcontact', 'verify', 'email'],
        "requires_connector": True,
        "verbs": ['verify', 'validate'],
        "produces": ['verification_result'],
        "consumes": ['email'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "api_entreprise_get_company_info",
        "required_fields": ['siret'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Get company information from API Entreprise.",
        "keywords": ['api', 'entreprise', 'get', 'company', 'info'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve'],
        "produces": ['company_info'],
        "consumes": ['siret'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "api_entreprise_search_companies",
        "required_fields": ['query'],
        "optional_fields": ['limit'],
        "permissions": "read",
        "description": "Search companies using API Entreprise.",
        "keywords": ['api', 'entreprise', 'search', 'companies'],
        "requires_connector": True,
        "verbs": ['search', 'find', 'query'],
        "produces": ['companies_list'],
        "consumes": ['query'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "CRM",
        "function": "api_entreprise_verify_company_certificates",
        "required_fields": ['siret'],
        "optional_fields": [],
        "permissions": "read",
        "description": "Verify company certificates using API Entreprise.",
        "keywords": ['api', 'entreprise', 'verify', 'company', 'certificates'],
        "requires_connector": True,
        "verbs": ['verify', 'check', 'validate'],
        "produces": ['certificate_status'],
        "consumes": ['siret'],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "jira_service_management_get_sla_status",
        "required_fields": [],
        "optional_fields": ['request_key', 'sla_breach_only'],
        "permissions": "read",
        "description": "Execute jira service management get sla status operation in Support.",
        "keywords": ['jira', 'service', 'management', 'get', 'sla', 'status'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    # WhatsApp Business API
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_send_message",
        "required_fields": ['phone_number', 'message'],
        "optional_fields": ['message_type', 'media_url', 'template_name'],
        "permissions": "write",
        "description": "Execute whatsapp business send message operation in Support.",
        "keywords": ['whatsapp', 'business', 'send', 'message'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_send_notification",
        "required_fields": ['phone_number', 'notification_type'],
        "optional_fields": ['template_data'],
        "permissions": "write",
        "description": "Execute whatsapp business send notification operation in Support.",
        "keywords": ['whatsapp', 'business', 'send', 'notification'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_get_messages",
        "required_fields": [],
        "optional_fields": ['phone_number', 'since', 'limit'],
        "permissions": "read",
        "description": "Execute whatsapp business get messages operation in Support.",
        "keywords": ['whatsapp', 'business', 'get', 'messages'],
        "requires_connector": True,
        "verbs": ['get', 'fetch', 'retrieve', 'list'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    
    funcs.append({
        "agent": "Support",
        "function": "whatsapp_business_analyze_conversation",
        "required_fields": ['phone_number'],
        "optional_fields": ['summarize'],
        "permissions": "read",
        "description": "Execute whatsapp business analyze conversation operation in Support.",
        "keywords": ['whatsapp', 'business', 'analyze', 'conversation'],
        "requires_connector": True,
        "verbs": ['execute'],
        "produces": [],
        "consumes": [],
        "status": "active"
    })
    return funcs
