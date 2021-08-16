import os
import openai
from dotenv import load_dotenv 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = """IE: Please generate 5 new labeled tickets based off of these sample tickets - [{"TalkDesk - Unable to login", "text_b": "Login/Access Hi I believe my account was deactivated by accident. I've received a message stating that my email address is not found.", "priority": "urgent"},
{"text_a": "Increase order quantity from 50 to 100", "text_b": "We have sent 50 copies of \"Frank Calderoni: Upstanding book FY22\", SKU: 560210, to Jeanne Rotenberry, at 9:15 AM CST, on June 30, 2021. We need to increase this order from 50 units to 100 units. Can you update this or should we cancel and resubmit? This order requires 2-day shipping.", "priority": "urgent"},
{"text_a": "Smart Recruiters  missing inventory", "text_b": "We got some blue light glasses delivered to the PHX warehouse back in April. However, it doesn't look like they were ever inventoried. Can you look further into this for us?", "priority": "high"},
{"text_a": "URGENT: Coffee Kits stuck in Customs for Italian Customers", "text_b": "I organized a send of coffee kits from the UK warehouse to clients in Italy. We sent this last week and have noticed that there were customs issues. Attached are some examples. This is especially urgent to us since we are incurring charges every day as these kits stay at customs. Do you know what caused this? What can we do to get these to their final destination? Who can we escalate this to? Is there an international team for issues like this? ", "priority": "urgent"}
{"text_a": "High Shipment Costs ?", "text_b": "Hi Team, Intercom reached out to me about seemingly high shipment costs. Is there a reason for these high costs and can we reduce these going forward? (orders attached). These are pre-kits and one from UK to Ireland was upwards of $50 in shipping.. Additionally, the customer states the quoting tool priced these at $21.", "priority": "high"}
{"text_a": "Link not sending to Authorize", "text_b": "Email is not sending to me.i hve checked junk and it is not in there as well. ", "priority": "normal"}
{"text_a": "Wrong items sent - again", "text_b": "Hello, We've had this issue in the past and it's happened again. The wrong size tee has been sent. Can you please re-send the correct size and solve this issue from the warehouse side so it doesn't happen again. Thanks", "priority": "urgent"}
{"text_a": "Need to add a new contact", "text_b": "Hi, I have a question about adding a new contact. I have attached a sample contact list. Can you please add me to the list and let me know if this is done. Thanks", "priority": "low"}
{"text_a": "Order to Siberia", "text_b": "Looks our only option to ship to Siberia from the UK is to use a non-tracked Royal Mail service. Please have support reach out to the sender and let them know. If they are good without tracking, please let us know so we can update the shipment method. I would also document the approval in case questions come up later on the selected ship method." "priority": "normal"}
{"text_a": "Invalid user", "text_b": "Hello Team, Could you help, I have an invalid user for some reason, see attached!" "priority": "low"}]\n AI: [{"text_a": "Tiled - Users not Assigned to Teams", "text_b": "Hello, I was on a call with my customer Tiled, and I reassigned the team owner to another person at the company. When I did that, the original team owner was not assigned to a Team, and I cannot find them in the platform. They exist in control panel, and when you go to User Spending Limit, their name is there and there is still money assigned to them. The person on the call wanted to delete them and assign their funds back to a funding source, but we couldn't find them. We even searched for the user and couldn't find them. This is troublesome for users that aren't assigned to a team. There isn't an easy way to find them. The new Teams UI is confusing. I have seen this with another customer as well. See screenshots attached for the scenarios I described above.", "priority": "urgent"},
{"text_a": "Electric- Charity Options", "text_b": "I'm trying to do the charity option, but I'm not finding a list of charities to choose from. I tested it on myself and it defaulted to \"KarmaKarma\" as the recipient charity.", "priority": "low"},
{"text_a": "Wrong Email attached to eGift", "text_b": "I recently received a eGift card from someone. Unfortunately, they entered the wrong email address in your system. It looks like I have to verify my email to redeem it, but the system will not accept it because the emails do not match. Is there any way you guys can update the email address? It is only one letter off. I would like to be able to redeem it. Thank you" "priority": "high"},
{"text_a": "Someone has logged into my account", "text_b": "Hi, it appears someone may have gotten access to my account and sent an e-gift. Can you help me look into this?", "priority": "urgent"},
{"text_a": "Can't add new contact", "text_b": "Hi, I have a question about adding a new contact. Your UI is pretty confusing and I cant seem to naviagte it to add this new user", "priority": "normal"}]
]
"""

response = openai.Completion.create(
  engine="davinci",
  prompt=prompt,
  temperature=0.3,
  max_tokens=300,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)