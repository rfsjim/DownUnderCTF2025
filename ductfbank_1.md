# Ductfbank 1
**Category** - AI <span style="color:blue;">Beginner</span>

## Challenge Text
I'm from DownUnderCTF Bank. As part of your company's business relationship with us, we are pleased to offer you a complimentary personal banking account with us. A link to our website is below. If you have any further queries, please don't hesitate to contact me!

Regards,
dot

## Goal
To get a flag from the DownUnderCTF Bank.

## Initial Observations
The DownUnderCTF Bank has a very basic web interface, that I can login to and once logged in there is a chat bot that I can interact with.

I have also given me the redacted ts code (looks like typescript) that powers the website and looks like the chat bot or at least the api running the chat bot.

First impressions are that prompt injections will be required to social engineer the bot into giving me the required information.

The code files provided are:
* agent_snip.ts - lists a number of tools that the agent can use most are beign operations tools you would expect this sort of banking agent to have but one is interestingly called flag
* bank_service.ts
* routes/ai.ts - authenticating users using java wev tokens and the hs256 algorithm.
* routes/dashboard.ts - Purely web layout tools
* routes/layouts.ts - Purely web layout tools
* routes/login.ts - Purely web layout tools

I want to understand the program flow, see if I can locate the agent's prompt template, looking for any filtering, escaping, or sanitising logic.

## Steps Taken
1. I started by using the sort of prompts I expected a bank to chat bot to respond to, based around the tools inside `agent_snip`.
2. I noticed that some queries would come back with an error similar to `I can not help with that enquiry`
2. I tried asking chatbot about accounts that were not linked to me, using similar account numbers and other identifiers based on the identifiers I could find for my bank account and using the parameters mentioned in tools. I noticed that the error changed to an authentication based error. This was valuable information, as it suggested that the AI agent **would** supply me with more information if I can make it think that I *should* have that information.
3. One tool that I noticed straight out of the code was a `create_account` tool
```ts
create_account: tool({
      description: 'REDACTED',
      parameters: z.object({
        nickname: z.string().describe("REDACTED")
      }),
      execute: async ({ nickname }) => {
        const account_number = await svc.createAccount(customerId, nickname);
        await svc.giveBonus(account_number);
        return { account_number };
      }
    }),
```
4. I asked the chatbot to create me a new account and I was given an account with $1,000 starting balance, entering the account I was given a flag, success. This challenge was completed.

See second challenge in set [Ductfbank 2](https://github.com/rfsjim/DownUnderCTF2025/blob/main/ductfbank_2.md)