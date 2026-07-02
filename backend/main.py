#!/usr/bin/env python
# coding: utf-8

# In[10]:


from dotenv import load_dotenv
import os
from langchain_openrouter import ChatOpenRouter
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from tools.customer_tools import *
from tools.account_tools import *
from tools.order_tools import *
from tools.payment_tools import *
from tools.shipment_tools import *
from tools.refund_tools import *
from tools.dashboard_tools import *
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from openai import OpenAI
# In[16]:

load_dotenv();



# In[17]:


# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to a database."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
]);

llm = AzureAIOpenAIApiChatModel(
    endpoint="https://models.github.ai/inference",
    credential=os.environ["GITLAB_API_KEY"], # Using your PAT
    model="gpt-4o",            # Specify the model here
    temperature=0.7
)

# In[18]:


tools = [
    get_customer,
    get_all_customers,
    search_customer,
    create_customer,
    update_customer_phone,
    activate_customer_account,
    deactivate_customer_account,
    delete_customer,
    customer_complete_summary,

    get_account,
    get_customer_accounts,
    deposit_money,
    withdraw_money,

    get_order,
    get_customer_orders,
    investigate_order_details,
    mark_order_delivered,

    get_payment,
    investigate_payment,
    list_failed_payments,

    get_shipment,

    investigate_refund,
    list_pending_refunds,

    dashboard_summary,
];
#llm_with_tools = llm.bind_tools(tools, tool_choice="none")
agent_executor = create_react_agent(llm, tools)


# In[19]:


def ask_agent(query):
    response = agent_executor.invoke({"messages": [("user", query)]})
    return response["messages"][-1].content


# In[20]:


print(ask_agent("Give the customer details for the Customer ID:1"));


# In[ ]:





# In[ ]:




