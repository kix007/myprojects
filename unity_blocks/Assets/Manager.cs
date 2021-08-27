using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Manager : MonoBehaviour
{
    public GameObject pandaItem, sheepItem, catItem,
        dogItem, elephantItem, cowItem,
        pandaSlot, sheepSlot, catSlot,
        dogSlot, elephantSlot, cowSlot;

    public AudioSource source;
    public AudioClip[] correct;
    public AudioClip incorrect;

    bool pandaCorrect, sheepCorrect, catCorrect,
        dogCorrect, elephantCorrect, cowCorrect = false;

    public GameObject score;
    public GameObject levelScore;
    private Text text;
    private Text LevelScoreText;
    public int scoreGet;
    private GameObject levelComplete;

    Vector2 pandaInitialPos, sheepInitialPos, catInitialPos,
        dogInitialPos, elephantInitialPos, cowInitialPos;

    // this function gets called when game loads
    public void Awake()
    {
        if(PlayerPrefs.HasKey("mycoin"))
        {
            scoreGet = PlayerPrefs.GetInt("mycoin");
        }
        else
        {
            scoreGet = 0;    
        }
        
    }
    
    
    // Start is called before the first frame update
    void Start()
    {
        pandaInitialPos = pandaItem.transform.position;
        sheepInitialPos = sheepItem.transform.position;
        catInitialPos = catItem.transform.position;
        dogInitialPos = dogItem.transform.position;
        elephantInitialPos = elephantItem.transform.position;
        cowInitialPos = cowItem.transform.position;

        text = score.GetComponent<Text>();
        LevelScoreText = levelScore.GetComponent<Text>();
        levelComplete = GameObject.FindGameObjectWithTag("LevelCompleteUI");

        levelComplete.SetActive(false);

    }

    public void DragPanda()
    {
        pandaItem.transform.position = Input.mousePosition;
    }

    public void DragSheep()
    {
        sheepItem.transform.position = Input.mousePosition;
    }

    public void DragCat()
    {
        catItem.transform.position = Input.mousePosition;
    }

    public void DragDog()
    {
        dogItem.transform.position = Input.mousePosition;
    }

    public void DragElephant()
    {
        elephantItem.transform.position = Input.mousePosition;
    }

    public void DragCow()
    {
        cowItem.transform.position = Input.mousePosition;
    }


    public void DropPanda()
    {
        float Distance = Vector3.Distance(pandaItem.transform.position, pandaSlot.transform.position);
        if(Distance<50)
        {
            pandaItem.transform.position = pandaSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            pandaCorrect = true;
            scoreGet = scoreGet + 1;
            pandaSlot.SetActive(false);
        }
        else
        {
            pandaItem.transform.position = pandaInitialPos;
            source.clip = incorrect;
            source.Play();
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }
    }

    public void DropSheep()
    {
        float Distance = Vector3.Distance(sheepItem.transform.position, sheepSlot.transform.position);
        if (Distance < 50)
        {
            sheepItem.transform.position = sheepSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            sheepCorrect = true;
            scoreGet = scoreGet + 1;
            sheepSlot.SetActive(false);
        }
        else
        {
            sheepItem.transform.position = sheepInitialPos;
            source.clip = incorrect;
            source.Play();
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }
    }

    public void DropCat()
    {
        float Distance = Vector3.Distance(catItem.transform.position, catSlot.transform.position);
        if (Distance < 50)
        {
            catItem.transform.position = catSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            catCorrect = true;
            scoreGet = scoreGet + 1;
            catSlot.SetActive(false);
        }
        else
        {
            catItem.transform.position = catInitialPos;
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }
    }

    public void DropDog()
    {
        float Distance = Vector3.Distance(dogItem.transform.position, dogSlot.transform.position);
        if (Distance < 50)
        {
            dogItem.transform.position = dogSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            dogCorrect = true;
            scoreGet = scoreGet + 1;
            dogSlot.SetActive(false);
        }
        else
        {
            dogItem.transform.position = dogInitialPos;
            source.clip = incorrect;
            source.Play();
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }
    }

    public void DropElephant()
    {
        float Distance = Vector3.Distance(elephantItem.transform.position, elephantSlot.transform.position);
        if (Distance < 50)
        {
            elephantItem.transform.position = elephantSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            elephantCorrect = true;
            scoreGet = scoreGet + 1;
            elephantSlot.SetActive(false);
        }
        else
        {
            elephantItem.transform.position = elephantInitialPos;
            source.clip = incorrect;
            source.Play();
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }
    }

    public void DropCow()
    {
        float Distance = Vector3.Distance(cowItem.transform.position, cowSlot.transform.position);
        if (Distance < 50)
        {
            cowItem.transform.position = cowSlot.transform.position;
            source.clip = correct[Random.Range(0, correct.Length)];
            source.Play();
            cowCorrect = true;
            scoreGet = scoreGet + 1;
            cowSlot.SetActive(false);
        }
        else
        {
            cowItem.transform.position = cowInitialPos;
            source.clip = incorrect;
            source.Play();
            if(scoreGet>0)
            {
                scoreGet = scoreGet - 1;
            }
            else
            {
                scoreGet = 0;
            }
        }

    }

    public void CorrectAnswer()
    {
        if(pandaCorrect && sheepCorrect && catCorrect &&
           dogCorrect && elephantCorrect && cowCorrect)
        {
            PlayerPrefs.SetInt("mycoin", scoreGet);
            // scoreGet = 1;
            levelComplete.SetActive(true);
        }

        text.text = scoreGet.ToString();
        LevelScoreText.text = scoreGet.ToString();
    }

    void Update()
    {
        CorrectAnswer();
    }
    //void Update ()
    //{
    //if(pandaCorrect && sheepCorrect && catCorrect && 
    //   dogCorrect && elephantCorrect && cowCorrect)
    //{
    //    Debug.Log("You win!");
    //    text.text = "1";
    //}
    //}
}
