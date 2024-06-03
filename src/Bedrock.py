from src.client_init import bedrock_agent_client, bedrock_client, accept, contentType
import json


# Retreive API call to Bedrock KB 
def dec_retrieve(query, kbId, numberOfResults=5):
    return bedrock_agent_client.retrieve(
        retrievalQuery= {
            'text': query
        },
        knowledgeBaseId=kbId,
        retrievalConfiguration= {
            'vectorSearchConfiguration': {
                'numberOfResults': numberOfResults
            }
        }
    )
# Invoke Bedrock
def invoke(*,prompt, modelID, max_tokens = 2056, temp = 0.5):
    message=[{ "role":'user', "content":[{'type':'text','text': prompt}]}]
    payload = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "messages": message,
        "temperature": temp,
        "top_p": 1
            }  )  
    
    response = bedrock_client.invoke_model(body=payload, modelId=modelID, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    return response_body.get('content')[0]['text']

def invoke_stable_diff(*, prompt, seed, height, width, cfg_scale = 10, steps = 30, style_preset=None):
    try:
        # The different model providers have individual request and response formats.
        # For the format, ranges, and available style_presets of Stable Diffusion models refer to:
        # https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-stability-diffusion.html

        body = {
            "text_prompts": [{"text": prompt}],
            "seed": seed,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "height": height,
            "width": width,
        }

        if style_preset:
            body["style_preset"] = style_preset

        response = bedrock_client.invoke_model(
            modelId='stability.stable-diffusion-xl-v1', body=json.dumps(body)
        )

        response_body = json.loads(response["body"].read())
        base64_image_data = response_body["artifacts"][0]["base64"]

        return base64_image_data

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}\n")
        raise

def invoke_titan_image(*, prompt, seed, width, height, cfgScale = 8):
    """
    Invokes the Titan Image model to create an image using the input provided in the request body.

    :param prompt: The prompt that you want Amazon Titan to use for image generation.
    :param seed: Random noise seed (range: 0 to 2147483647)
    :return: Base64-encoded inference response from the model.
    """

    try:
        # The different model providers have individual request and response formats.
        # For the format, ranges, and default values for Titan Image models refer to:
        # https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-image.html

        request = json.dumps(
            {
                "taskType": "TEXT_IMAGE",
                "textToImageParams": {"text": prompt},
                "imageGenerationConfig": {
                    "numberOfImages": 1,
                    "cfgScale": cfgScale,
                    "height": height,
                    "width": width,
                    "seed": seed,
                },
            }
        )

        response = bedrock_client.invoke_model(
            modelId="amazon.titan-image-generator-v1", body=request
        )

        response_body = json.loads(response["body"].read())
        base64_image_data = response_body["images"][0]

        return base64_image_data

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}\n")
        raise



